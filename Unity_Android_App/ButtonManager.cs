using System.Collections;
using System.Collections.Generic;
using UnityEngine; 

using SharpConnect; // enables the creation of new Connector instance. Imports the namespace defined in TCP_IP_client script
using UnityEngine.UI; // enables displaying text on phone screen
using System.Threading; // enables using Thread.sleep

public class ButtonManager : MonoBehaviour {

// declare variables

	// function accessing info provided by Manomotion's SDK info (ex: hand position and relative depth)
	public HandTrackerManager htm; 

	// text can be visualize on phone screen. it needs to be attributed to an object in unity 
	[SerializeField]
	public Text connectionStatusText, realWorld, Z_Value, handState, noise;

	bool connected_to_websocket;

	int NewState;
	int Frame;

	string connectionStatus;
	// refer to	public class Connector in script "TCP_IP_client"
	Connector myConnector= new Connector();

	public Vector3 palmToWorld;
	public Vector3 palmRaw;
	public float WidthImagePlane;
	public float HeightImagePlane;
	public float XinMeters;
	public float ZinMeters;
	public float YinMeters;
	public float rel_depth;



	void Start (){

		connected_to_websocket = false;
	}




	void Update() {
		
		// User's feedback: display warnings on screen
		if (htm.GetManomotionGesture ().flag == 0) {
			noise.text = "No warning ";
		}

		if (htm.GetManomotionGesture ().flag == 1) {
			noise.text = "Warning: hand not found";
		}
			
		if (htm.GetManomotionGesture ().flag == 2) {
			noise.text = "Warning: change background";
		}

		if (htm.GetManomotionGesture ().flag == 3 || htm.GetManomotionGesture ().flag == 4 || htm.GetManomotionGesture ().flag == 5 || htm.GetManomotionGesture ().flag == 6 ) {
			noise.text = "Warning: hand approaching edge ";
		}


		if (htm.GetManomotionGesture ().flag == 7) {
			noise.text = "Warning: hand too close";
		}


		if (htm.GetManomotionGesture ().flag == 8) {
			noise.text = "Warning: noisy";
		}


		Debug.Log ("TOWEBSOCKETFLAG_getmanomotiongesture" + htm.GetManomotionGesture ().flag);
		Debug.Log ("TOWEBSOCKETFLAG_htm" + HandTrackerManager.Flags.FLAG_NOISE);


		// display on screen: normalized depth value and current hand state
		Z_Value.text = "Relative depth: " + htm.GetManomotionGesture ().relative_depth.ToString();
		handState.text =  "Hand state: " + htm.GetManomotionGesture ().state.ToString();



		// retrieves 3D world coordinates of the hand
		Vector3 palmRaw=htm.PalmCenter; // vector3 will contain pixel location in x and y and relative normalized depth
	
		// mapping normalized depth value to absolute value
		rel_depth=htm.GetManomotionGesture ().relative_depth;
		palmRaw.z = 0.45f*rel_depth;  

		// retrieves hand coordinates
		Vector3 palmToWorld =  Camera.main.ScreenToWorldPoint (palmRaw);

		// multiply with the scaling factors
		XinMeters=palmToWorld.x*0.603f; 
		YinMeters=palmToWorld.y*0.905f;
		ZinMeters = palmToWorld.z * (palmRaw.z/1.45f); // z in meters should be the same z as the distance from the camera to ground

		// display on screen: hand coordinates 
		realWorld.text = "Hand coordinates x, y, z: " +(XinMeters.ToString ("0.0000") + "," + YinMeters.ToString ("0.0000") + "," + ZinMeters.ToString ("0.0000"));

		// check info transmitted to websocket; get current hand state and frame number
		NewState = htm.GetManomotionGesture ().state;
		Frame=htm.GetManomotionGesture ().frame; 
		Debug.Log( "TOWEBSOCKET"+"<"+ Frame +"_" + NewState + "_"+ XinMeters.ToString("0.0000") + "_"+ YinMeters.ToString("0.0000")+ "_"+ ZinMeters.ToString("0.0000")+ ">");

		// send info bundle to the server
		if (connected_to_websocket) {
				SendHandInfo ();
		}
			
	}




	// define what info should be transmited to the server
	public void SendHandInfo()
	{
		string InfoBundle = "<"+ Frame +"_" + NewState + "_"+ XinMeters.ToString("0.0000") + "_"+ YinMeters.ToString("0.0000")+ "_"+ ZinMeters.ToString("0.0000")+ ">";
		myConnector.SendData(InfoBundle);
		Debug.Log("TOWEBSOCKETsentInfoBundle"+ InfoBundle);
		Thread.Sleep (1);

	}


    // define client settings such as IP
	public void ToggleConnection(){


		if (!connected_to_websocket) {
			//I need to connect
			Debug.Log("Connected");
			//Fill in the requirements of the  myConnector.fnConnectResult ();
			string sNetIP="192.168.20.230";
			int iPORT_NUM = 8080;
			string sUserName = "RoxanaAndTenMoreCharacters";
			connectionStatus = myConnector.fnConnectResult (sNetIP,iPORT_NUM,sUserName);
			//This method, if it succeeds will give you back a text message.
			//Since its a string you should compare it with the outcome you want to see if its succeeded
			//*If you want, you could instead return 0 for succeed and 1 for fail to have the checking of connection easier.
			if (connectionStatus == "Connection Succeeded") {
				//This is the confirmation that you have been connected.
				connected_to_websocket = true;
				connectionStatusText.text = "Connected";

			} else {
				connectionStatusText.text = "Connection Error";
				Debug.Log ("Not connected");
			}


		} else {
			//Disconnect
			connected_to_websocket = false;

		}

	}




}	
