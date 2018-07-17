#!/usr/bin/env python

import socket
from multiprocessing import Process,Value,Array,Pipe,Pool
import time
import rospy
from std_msgs.msg import String

## Defining Macros
#IP_ADDR="192.168.20.191"
IP_ADDR=''				# Use '' for automatically select the local machine's IP
PORT=8080				# Select a port for communication
MSGLEN= 2				# expected incoming message length

dummy1 = 0
dummy2 = 1

class serverSocket:
	""" Server Socket class: Defines the server socket for communication between clients and also provides methods for reading and writing using socket""" 
	def __init__(self, sock=None):
		""" Initialize the server socket which is set to communicate using internet and of type STREAM.This method also initializes the clientSocket object and its address."""
        	if sock is None:
	            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        	else:
	            self.sock = sock	# For user defined sockets
		self.clientSocket=None
		self.cAddress=None

	def serverBind(self, host, port):
		""" Method for binding the given host IP and port to the previously created server socket and sets the socket to listen to incoming connections"""
        	self.sock.bind((host, port))
		self.sock.listen(5)

	def serverAcceptConnections(self):
		""" This method runs a loop which accepts any incoming connection and return the clientSocket object and its corresponding address"""
		try:
			while self.clientSocket is None:
				print "Waiting for connection from client"
				(self.clientSocket,self.cAddress)=self.sock.accept()
			print "Connected to Client Address:",self.cAddress
		except IOError as e:
    			print "I/O error({0}): {1}".format(e.errno, e.strerror)

		return self.clientSocket,self.cAddress

	def sockWrite(self, msg):
		""" Sample method to write to the client using the socket"""
        	totalsent = 0
	        while totalsent < MSGLEN:
        	    sent = self.sock.send(msg[totalsent:])
	            if sent == 0:
        	        raise RuntimeError("socket connection broken")
	            totalsent = totalsent + sent

	def sockRead(self):
		""" Sample method to read from the clientSocket"""

        	chunks = []
		data=[]
	        bytes_recd = 0
		data=self.clientSocket.recv(64)
        	#while bytes_recd < MSGLEN:
	        #    chunk = self.clientSocket.recv(min(MSGLEN - bytes_recd, 2048))
        	#    if chunk == '':
                #	raise RuntimeError("socket connection broken")
	        #    chunks.append(chunk)
        	#    bytes_recd = bytes_recd + len(chunk)
#	        return ''.join(chunks)
		#print "data:" , data
		start = data.find("<") 
		end = data.find(">")
		#print start,end
		if  start > -1:
			if end > start:
				data = data[start+1 : end]
				#print "Data", data 
				data = data.split('_')
				
				return data			
		else:
			pass
				
			 		

###Publisher

# license removed for brevity

 
def talker(dummy1, dummy2):
     	pub = rospy.Publisher('chatter', String, queue_size=10)
     	rospy.init_node('talker', anonymous=True)
     	#rate = rospy.Rate(10) # 10hz
     	while not rospy.is_shutdown():
	 	ran = soc.sockRead() # Read message of MSGLEN from the client
         	hello_str = ran
		#print("type ran",type(hello_str))
		
		if str(type(hello_str)) == "<type 'list'>": 
			#if len(hello_str) > 2:
				data = ran 
				#print("data",data)
				if dummy2 == 1:
					frame = int(data[0])
					hand_avg = [int(data[1]), int(data[1]), int(data[1]), int(data[1]), int(data[1])]
					x_avg = [float(data[2]), float(data[2]), float(data[2]), float(data[2]), float(data[2])]
					y_avg = [float(data[3]), float(data[3]), float(data[3]), float(data[3]), float(data[3])]
					z_avg = [float(data[4]), float(data[4]), float(data[4]), float(data[4]), float(data[4])]
					dummy2 = 0
						

				#print("dummy1",dummy1)
				frame = int(data[0])
				hand_avg[dummy1] = int(data[1])
				x_avg[dummy1] = float(data[2])
				y_avg[dummy1] = float(data[3])
				z_avg[dummy1] = float(data[4])
				
				hand = int(sum(hand_avg)/5)
				x = float(sum(x_avg)/5)
				y = float(sum(y_avg)/5)
				z = float(sum(z_avg)/5)
				

				frame = str(frame)
				hand = str(hand)
				x = str(x)
				y = str(y)
				z = str(z)
				info = frame+"_"+hand+"_"+x+"_"+y+"_"+z


				#print("info",info)
				dummy1 = dummy1 + 1
				if dummy1 == 5:
					dummy1 = 0 	 

				rospy.loginfo(hello_str)
				pub.publish(info)
        			#rate.sleep()
	 




if __name__=="__main__":
	""" Sample usage of the class serverSocket"""

	try:
		soc=serverSocket()			# Creating a socket object
		soc.serverBind(IP_ADDR,PORT)		# Binding the socket obeject to the host IP and port
		clSock,addr=soc.serverAcceptConnections() # Accept incoming connection 	from client
			
		talker(dummy1, dummy2)						
		#soc.sockWrite("Hi")			# Sample write message
	except(KeyboardInterrupt) or rospy.ROSInterruptException:
		print "Keyboard Interrupt. Closing socket connection..."
		clSock.close()
		print "Socket closed"
		pass
