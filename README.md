# Iniciando AWS IoT

En este repositorio vamos a aprender los primeros pasos para integrarnos a mundo de AWS IoT. 


Para conocer las ventajas y caracteristicas del mundo AWS IoT te inivito a visitar el siguiente link: [https://aws.amazon.com/es/iot/](https://aws.amazon.com/es/iot/)


Este tutorial consiste en tres ejercicios un primer ejercicio donde simularemos un dispositivo utilizando un programa simple en Python y otro usando un dispositivo real NodeMCU ESP8266, ambos para enviar mensajes a la nube AWS IoT Core, y en un tercero ejercicio cofiguraremos algunas acciones gatilladas con los mensajes enviados. 

---
---

## AWS IoT Core 


AWS IoT Core es un servicio en la nube administrado que permite a los dispositivos conectados interactuar de manera fácil y segura con las aplicaciones en la nube y otros dispositivos.

!["AWS IoT Core"](imagen/AWS_IoT_Core.png)

[Conoce más sobre AWS IoT Core](https://aws.amazon.com/es/iot-core/?nc=sn&loc=2&dn=3)

---
---

## Ejercicio 1: Enviar mensajes MQTT a AWS IoT Core desde Python. 

En este ejercicio, vamos a configurar un objeto de IoT en AWS IoT Core; una vez que tenga esa configuración, ejecutaremos un pequeño programa para simular el envío de datos a AWS IoT Core y luego usará el cliente de prueba MQTT para ver la carga útil de cada mensaje MQTT.

!["Ejericio 1"](imagen/ejercicio1.png)

¿Que necesitas?

- [x] Una cuenta AWS. [Crea tu cuenta con capa gratuita](https://aws.amazon.com/es/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc)
- [x] Conocimientos en Python.
- [x] Configurada tus credenciales de acceso de la cuenta AWS. [Aca como lo puedes hacer](https://docs.aws.amazon.com/es_es/cli/latest/userguide/install-cliv2.html)

---

### Parte 1: Crear el objeto en AWS IoT Core.


Ir al servicio AWS IoT Core

!["Paso 1"](imagen/paso1.png)


En el siguiente menú seleccionar Click a **"Crear solo un objeto"**

Para este ejercicio le colocaremos el nombre de **objeto1** y le damos Click a **"Siguiente"**

En el siguiente paso debes darle Click a **"Crear Certificado"**
 

Un certificado X.509 individual por dispositivo es la forma recomendada de interactuar con los servicios de AWS IoT desde los dispositivos, 
lo que ofrece la capacidad de grabar la clave privada en el dispositivo al momento de la inscripción que luego nunca se transfiere a través de Internet junto con las solicitudes, una ventaja de seguridad. 


 !["Descargar Certificados"](imagen/paso1a.png)

 Descargue el certificado y la clave privada para el dispositivo, y también el rootCA 1 . 

- Modifica el nombre de tu certificado a **certificate.pem**
- Modifica el nombre de tu private key a **privateKey.pem**
- Modifica el nombre de tu rootCA 1 a **rootCA.pem**

 Asegúrese de presionar el botón de **"Activar"** para que se pueda usar el certificado. 


 !["Descargar CA 1"](imagen/paso1b.png)

Finalice el proceso haciendo clic en el botón **"Listo"**. 

El siguiente punto es crear y adjuntar una política al certificado, que autorice al dispositivo autenticado a realizar acciones de IoT en los recursos de IoT.

Para crear la politica debes ir al menú del lado izquierdo **Seguridad -> Políticas** una vez ahí debes darle Click a **"Crear una Política"**, para efectos de este ejercicio la nombreremos **objeto1-policity**, complete los campos (Acción, ARN de recurso) con una estrella **"*"**, esto solo para efectos de este ejerccio ya que permite todo, y marque la opción Permitir efecto y luego presione el botón **"Crear"**.

Ahora en el menú del lado izquierdo **Seguridad -> Certificados**, verá el certificado que ha creado anteriormente, toque los tres puntos de la derecha y elija **Asociar política**, aparecerá una ventana emergente que muestra sus políticas existentes, verifique las recientes política que haya creado y asocie.

**¡¡Esto es todo Felicidades!! ya has creado tu primer objeto de AWS IoT con éxito, le has generado un certificado y le has adjuntado una política.**

---

### Parte 2: Simular dispositivo con programa en python.

En esta parte debes descargar el siguiente programa [ejercicio1.py](https://github.com/elizabethfuentes12/Iniciando_AWS_IoT/blob/master/ejercicio1.py) en la misma carpeta donde tienes los certificados descargados y renombrados en la parte anterior. 

Para que el programa funcione debes modificar lo siguiente: 

- Asegurate de tener configurada tus credenciales de acceso de la cuenta AWS. [Aca como lo puedes hacer](https://docs.aws.amazon.com/es_es/cli/latest/userguide/install-cliv2.html)

- En AWS Iot Core vas al menu de abajo a la izquierda en **"Coniguración -> Punto de enlace"** y copias y pegas aca el link que aparece en la siguiente linea reemplazando a "data.iot.us-west-2.amazonaws.com":
```
mqttc.configureEndpoint("data.iot.us-west-2.amazonaws.com",8883)
```
- Debes asegurarte que el nombre de tus certificados tenga los nombres a continuación y además que esten en la misma carpeta. 

```
mqttc.configureCredentials("./rootCA.pem","./privateKey.pem","./certificate.pem")
```
Configura el ambiente para ver los datos antes de activar el programa: 

Ve al menu de abajo a la izquierda **"Prueba"** y en Publicar especifica el mensaje que para nuestro caso de llama **"data"**, como lo puedes ver en e codigo. 

```
mqttc.publish("data", message, 0)
```

!["Configurar la prueba"](imagen/paso2.png)

Finalizas dandole click a **"Suscribirse al tema"**

Ahora ejecuta el programa 

```
python ejercicio1.py
```

y si todo esta OK podrias empezar a ver la información. 

!["Resultado paso2"](imagen/paso2a.png)

Para cancelar la ejecucion debes presionar **"ctrl + c"**

## Ejercicio 2: Enviar mensajes MQTT a AWS IoT Core desde NodeMCU ESP8266.

En este ejercicio usaremos el mismo objeto creado en el paso anterior. 

!["Ejericio 2"](imagen/ejercicio1.png)

¿Que necesitas?

- [x] Una cuenta AWS. [Crea tu cuenta con capa gratuita](https://aws.amazon.com/es/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc)
- [x] Un NodeMCU ESP8266. Disponible en cualquier tienda on-line [ejemplo](https://www.amazon.com/-/es/Internet-desarrollo-inalámbrico-funciona-Micropython/dp/B07R4MVSCY/ref=sr_1_6?__mk_es_US=ÅMÅŽÕÑ&dchild=1&keywords=NodeMCU+ESP8266&qid=1600307883&sr=8-6).
- [x] Tener instalado en tu computador Arduino. [Link de descarga](https://www.arduino.cc/en/main/software)

Puedes conocer un poco mas de NodeMCU en su [Datasheet](hhttps://www.esploradores.com/datasheet-nodemcu/)


## Ejercicio 3: Manejo de mensajes IoT en AWS Cloud.

### Parte 1: Crear una tabla DynamodDB con mensajes MQTT desde AWS IoT Core

Primero que todo debemos crear una tabla en DynamondDB, para esto debemos ir al servicio con su nombre y darle click en **"Crear Tabla"**, para nuestro ejercicio la nombraremos **"iot-prueba"** para las Claves principales usaremos los datos que enviamos desde nuestro programa **ID** y **Fecha**.

!["Crer Tabla DynamodDB"](imagen/crear_tabla.png)

Una vez creada la tabla vamos al servicio AWS IoT Core 









