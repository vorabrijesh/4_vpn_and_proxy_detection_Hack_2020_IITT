import shodan

# Setup the API wrapper
api = shodan.Shodan('c4D4wJe0kdCyDOI60sAP4GEwCfkmj0mK') # Free API key from https://account.shodan.io

# Lookup the list of services an IP runs
IP = "185.220.101.34"
ipinfo = api.host(IP)
#print(ipinfo)
# Check whether the IP runs a VPN service by looking for the "vpn" tag
if 'tags' in ipinfo and 'vpn' in ipinfo['tags']:
    print('{} is connecting from a VPN'.format(IP))

# Print general info
print("""
        IP: {}
        Organization: {}
        Operating System: {}
""".format(ipinfo['ip_str'], ipinfo.get('org', 'n/a'), ipinfo.get('os', 'n/a')))

# Print all banners
for item in ipinfo['data']:
        print("""
                Port: {}
                Banner: {}

        """.format(item['port'], item['data']))

