# following code brings whois record for a given ip address
from ipwhois import IPWhois

obj = IPWhois('139.99.159.15') #Enter your ip address here 

res=obj.lookup_whois()

print(res)