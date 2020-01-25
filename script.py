
import re 

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
	

def checkip(Ip): 


	if(re.search(regex, Ip)): 
		print("Valid Ip address") 
		
	else: 
		print("Invalid Ip address") 
	

def check(ip):
	flag=0
	with open('proxy.txt') as f:
		if ip in f.read():
			flag=1
			print("true")
		if flag==0:
			print("false")


if __name__ == '__main__' : 
	
	Ip = "41.196.237"
	checkip(Ip)
	check(Ip)