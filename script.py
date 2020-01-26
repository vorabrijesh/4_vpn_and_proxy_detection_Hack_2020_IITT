
import re 
import socket
import binascii


def check(ip):
	flag=0
	with open('sure_results.txt') as f:
		if ip in f.read():
			flag=1
			print("true")
		if flag==0:
			print("false")


def ip_to_int(ip_address):
	for version in (socket.AF_INET, socket.AF_INET6):
		try:
			ip_hex = socket.inet_pton(version, ip_address)
			Ip = int(binascii.hexlify(ip_hex), 16)
			return Ip
		except:
			pass
	raise ValueError("invalid IP address")


if __name__ == '__main__' :
	ip_address='180.168.49.108'
	Ip = ip_to_int(ip_address)
	check(str(Ip))
	
	
	
