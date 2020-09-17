# Instalación de OpenSSL: 

Es una herramienta que proporciona una implementación de código abierto de los protocolos SSL y TLS y que se puede utilizar para convertir los archivos de certificado en el más popular basado en X.509 v3 formatos. aquí lo usaremos para convertir los archivos .pem a .DER.

## OpenSSL on Linux

Si está usando Linux, puede instalar OpenSSL con el siguiente comando de consola YUM:If you’re using Linux, you can install OpenSSL with the following YUM console command:

```
$ yum install openssl
```

Si su distribución se basa en APT en lugar de YUM, puede usar el siguiente comando en su lugar:

```
$ apt-get install openssl
```

## OpenSSL on Windows

Si está utilizando Windows, puede instalar una de las muchas implementaciones de código abierto de OpenSSL: la que podemos recomendar es Win32 OpenSSL de Shining Light Production, disponible como versión ligera o completa, ambas compiladas en x86 (32 bits) y Modos x64 (64 bits). Puede instalar cualquiera de estas versiones, siempre que su sistema las admita.

### IMPORTANTE: OpenSSL para Windows requiere el tiempo de ejecución de Visual C ++ 2008 Redistributables para funcionar.

OpenSSL es básicamente una aplicación de consola, lo que significa que la usaremos desde la línea de comandos: después de que se complete el proceso de instalación, es importante verificar que la carpeta de instalación (C: \ Archivos de programa \ OpenSSL-Win64 \ bin para el 64- bit) se ha agregado al PATH del sistema (Panel de control> Sistema> Avanzado> Variables de entorno): si no es el caso, recomendamos encarecidamente agregarlo manualmente, para que pueda evitar escribir la ruta completa del ejecutable cada vez deberá iniciar la herramienta.