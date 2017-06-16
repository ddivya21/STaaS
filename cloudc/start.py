#!/usr/bin/python

import os,sys,commands,time,socket
s_ip="192.168.122.79"
s_port=7777
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

drive_name=raw_input("Enter drive name : ")
drive_size=raw_input("Enter drive size in GB : ")

s.sendto(drive_name,(s_ip,s_port))
s.sendto(drive_size,(s_ip,s_port))

res=s.recvfrom(4)
if res[0]=="done" :
	os.system('mkdir /media/'+drive_name)
	os.system('mount '+s_ip+':mnt/'+drive_name+' /media/'+drive_name)
else:
	print "No response from Storage Cloud"

