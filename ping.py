
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
	param = '-n' if platform.system().lower()=='windows' else '-c'
	command = ['ping', param, '1', host]
	return subprocess.call(command) == 0
	
hos = input()
ping(hos)