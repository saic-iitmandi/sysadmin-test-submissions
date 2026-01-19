
import os
import platform
import subprocess
import sys

# Defining variables

proxy ="http://10.7.0.1:8080"
wifi_name1="IITMandi_5.0 GHz"
wifi_name2="IITMandi_2.4 GHz"

# printing os platforms
print("System Platform : ",platform.system())
print(sys.argv)
if(len(sys.argv)>2):
	print("""usage : wifi_Proxy_script.py <switch>
		-s : to set proxy setting for given wifi network
		-u : to unset proxy settings
		-h : help""")
else:
	if ("-s" in sys.argv):
		# for window systems 
		if (platform.system()=="Windows"):
			wifi= subprocess.check_output("netsh wlan show interfaces").decode('utf-8')
			if (wifi_name1 in wifi) or (wifi_name2 in wifi):
				os.environ['HTTP_PROXY'] = proxy
				os.environ['HTTPS_PROXY'] = proxy
				print("Enviroment variable for HTTP_PROXY and HTTPS_PROXY is set")

		# for linux systems
		if (platform.system()=="Linux"):
			wifi= subprocess.check_output("iwgetid -r").decode('utf-8')
			if (wifi_name1 in wifi) or (wifi_name2 in wifi):
				os.environ['HTTP_PROXY'] = proxy
				os.environ['HTTPS_PROXY'] = proxy
				print("Enviroment variable for HTTP_PROXY and HTTPS_PROXY is set")
	if ("-u" in sys.argv):		
		os.environ['HTTP_PROXY'] = ''
		os.environ['HTTPS_PROXY'] = ''
		print("Enviroment variable for HTTP_PROXY and HTTPS_PROXY is unsetted.")
	if ("-h" in sys.argv):	
		print("""usage : wifi_Proxy_script.py <switch>
		-s : to set proxy setting for given wifi network
		-u : to unset proxy settings
		-h : help""")


