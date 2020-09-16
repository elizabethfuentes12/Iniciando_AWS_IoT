# Iniciando AWS IoT

En este repositorio vamos a aprender los primeros pasos para integrarnos a mundo de AWS IoT. 


Para conocer las ventajas y caracteristicas del mundo AWS IoT te inivito a visitar el siguiente link: [https://aws.amazon.com/es/iot/](https://aws.amazon.com/es/iot/)


Este tutorial consiste en dos ejercicios uno usando python y otro usando un NodeMCU ESP8266, en ambos trabajaremos en el servicio AWS IoT Core. 

---

## AWS IoT Core 


AWS IoT Core es un servicio en la nube administrado que permite a los dispositivos conectados interactuar de manera fácil y segura con las aplicaciones en la nube y otros dispositivos.

!["AWS IoT Core"](AWS_IoT_Core.png)

[Conoce más sobre AWS IoT Core](https://aws.amazon.com/es/iot-core/?nc=sn&loc=2&dn=3)

---

## Ejercicio 1:

En este ejercicio, vamos a configurar un objeto de IoT en AWS IoT Core; una vez que tenga esa configuración, ejecutaremos un pequeño programa para simular el envío de datos a AWS IoT Core y luego usará el cliente de prueba MQTT para ver la carga útil de cada mensaje MQTT.

¿Que necesito?

- [x] Una cuenta AWS. [Crea tu cuenta con capa gratuita](https://aws.amazon.com/es/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc)
- [x] Tener instalado un compilador de Python (Anaconda, Visual Studio Code, etc..)

  [Descargar Anaconda](https://www.anaconda.com/products/individual)
  
  [Descargar Visual Studio](https://code.visualstudio.com/download)

- [x] Conocimientos en Python, para entender el código. 



### Parte 1: Crear el objeto.


Ir al servicio AWS IoT Core

!["Paso 1"](paso1.png)


En el siguiente menú seleccionar Click a **"Crear solo un objeto"**

Para este ejercicio le colocaremos el nombre de **objeto1** y le damos Click a **"Siguiente"**

En el siguiente paso debes darle Click a **"Crear Certificado"**
 

Un certificado X.509 individual por dispositivo es la forma recomendada de interactuar con los servicios de AWS IoT desde los dispositivos, 
lo que ofrece la capacidad de grabar la clave privada en el dispositivo al momento de la inscripción que luego nunca se transfiere a través de Internet junto con las solicitudes, una ventaja de seguridad. 

Descargue el certificado y la clave privada para el dispositivo, y también el CA 1 . 

Asegúrese de presionar el botón de **"Activar"** para que se pueda usar el certificado. 

 !["Descargar Certificados"](paso1a.png)
 
 !["Descargar CA 1"](paso1b.png)

Finalice el proceso haciendo clic en el botón "Listo". 







