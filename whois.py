from ipwhois import IPWhois
import sys 
import ipwhois
    
 #Enter your ip address here 


try:
  obj = IPWhois('10.21.131.7')
except ipwhois.exceptions.IPDefinedError:
  res = {}
else:
  res = obj.lookup()

if (res=={}):
	print('Private Network')
	sys.exit()
j=1
for i in res:
	
	if(i=='nets'):
		print(j,i," :    ",type(res[i]))
		str1=str(res[i])
		str1=str1.split(",")
		for k in str1:
			print('         ',k)
	else:
		print(j,i,' : ',res[i])

	j=j+1
