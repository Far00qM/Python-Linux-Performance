#!/usr/bin/python
import os
import subprocess
import sys # package to accept input hostname/ipaddress

command= "ssh " + sys.argv[1] + " vmstat"                    
vm = subprocess.check_output("%s" %command, shell = True)  # getting command output from remote host

vm1 = vm.splitlines()
vm2 = vm1[2].split()
sw_in = vm2[6]
sw_ot = vm2[7]
bi = vm2[8]
bo = vm2[9]



command1= "ssh " + sys.argv[1]+ " uptime"
vm = subprocess.check_output("%s" %command1, shell = True) # getting command output from remote host

def upti():
 ut = subprocess.check_output("%s" %command1, shell = True)
 ut1 = ut.splitlines()
 ut2 = ut1[0].split()
 ut3 = float(ut2[9])
 com_cpu = "cat /proc/cpuinfo | grep 'cpu cores' | awk '{print $4 }'"
 cpcors = subprocess.check_output("%s" %com_cpu, shell=True)
 total_cpu = 100*ut3/float(cpcors)
 print("cpu load is at %s" %total_cpu)  # calculating the load average per cpu cores
 print("done")

def mem_usage():
 if sw_in or sw_ot < 0 : # data is move to swap memory as main memory is used
  print( " you may need to increase memory as swap_in and out is more %s and %s" %(sw_in,sw_ot) )



if vm2[0] <  vm2[1]: # more queue process for cpu
 print("issue could be because of CPU as queue values are %s and %s " %(vm2[0],vm2[1]))
 upt1 = upti()
 print(upt1)
 if vm2[9] < vm2[10]: #  more queue process for memory, disk or network
  print("issue could be because of more system process ")
 else:
  print("issue could be because of high user process")#
else:
 print("issue could be becase of network or memory or storage")
 mem_det = mem_usage()
 print("check top command to find the process with high cpu or memorary usage")

