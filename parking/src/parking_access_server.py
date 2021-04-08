#!/usr/bin/env python

import rospy
from parking.srv import *
from std_msgs.msg import String
import json

def server_request(request):
	global json_dict
	parking_id=request.parking_id.data
	state_parking=request.state_parking.data
	json_dict["parking_%d"%(parking_id)]=state_parking	
	response=parking_stateResponse()
	response.res_srvr.data=True
	return response	
		

def access_server():
	global json_dict
	rospy.init_node("parking")
	rospy.Service("parking_access_server", parking_state, server_request)
	pub=rospy.Publisher("parking_state",String, queue_size=10)
	rate=rospy.Rate(10)
	
	### (0:free, 1:occupied, 2:reserved)	
	json_dict={
	"parking_1":0,
	"parking_2":0,
	"parking_3":0,
	"parking_4":0		
	}
	while not rospy.is_shutdown():
		json_msg=json.dumps(json_dict)
		pub.publish(json_msg)
	#rospy.spin()

if __name__== '__main__':
	access_server()
