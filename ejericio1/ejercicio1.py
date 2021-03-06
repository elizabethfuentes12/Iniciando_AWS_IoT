#!/usr/bin/python

# ejercicio 1 - Simulador de Dispositivo con Python.
# Asegurate que tu region tu hosts esten correctos. 

import sys
import ssl
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
from datetime import datetime
import random


#Conigura tu MQTT cliente y tus certificados. Setup our MQTT client and security certificates
#Asegurate que el nombre de tus certificados coincida. 

mqttc = AWSIoTMQTTClient("1234")

#Debes pegar en Endpoint de tu dispositivo. 
#El endpoint se encuentra en el menu de la izquierda coniguracion -> punto de enlace y copias y pegas aca el link que aparece. 

mqttc.configureEndpoint("data.iot.us-west-2.amazonaws.com",8883)
mqttc.configureCredentials("./rootCA.pem","./privateKey.pem","./certificate.pem")

#Función para crear una carga útil en JSON


def json_encode(string):
        return json.dumps(string)

mqttc.json_encode=json_encode

#Aca enviamos nuestro mensaje a iot topic

def send():
    mqttc.publish("data", message, 0)
    print ("Mensaje Publicado")
    #conectando al gateway
mqttc.connect()
print ("Conectado")


#Loop until terminated
while True:
    now = datetime.now()
    #Declarando las variables
    message ={
    'ID': str(random.randint(0,10)),
    'Temperatura': random.randint(30,50),
    'Fecha': str(now.strftime("%Y-%m-%d %H:%M:%S")),
    'Evento': str(random.randint(100,500))
    }
    #decodificando el JSON
    message = mqttc.json_encode(message)
    print(message)
    send()
    time.sleep(5)

mqttc.disconnect()

#To check and see if your message was published to the message broker go to the MQTT Client and subscribe to the iot topic and you should see your JSON Payload

