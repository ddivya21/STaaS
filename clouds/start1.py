#!/usr/bin/python

import os,sys,commands,time,socket
s_ip=""
s_port=7777
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((s_ip,s_port))

#Receiving drive name, drive size and client address
data=s.recvfrom(20)
data1=s.recvfrom(10)
d_name=data[0]
d_size=data1[0]
cliaddr=data1[1][0]

#Creating logical volume
#os.system('lvcreate --size '+d_size+'M --thin novavg/pool1')
os.system('lvcreate -V'+d_size+'G --name '+d_name+' --thin novavg/pool1')

#Displaying logical volume
os.system('lvdisplay')

#Formatting client drive with ext4/xfs
os.system('mkfs.xfs /dev/novavg/'+d_name)

#Creating directory by name of client's drive
os.system('mkdir /mnt/'+d_name)

#Mounting client's drive
os.system('mount /dev/novavg/'+d_name+' /mnt/'+d_name)

#Installing nfs-utils
os.system('yum install nfs-utils -y')

#Making entry in nfs exports file
entry='/mnt/'+d_name+' '+cliaddr+'(rw,no_root_squash)'
f=open('/etc/exports','a')
f.write(entry)
f.write("\n")
f.close()
check=os.system('exportfs -r')

if check==0 :
	s.sendto("done",data1[1])
else :
	print "Please check your code !"

