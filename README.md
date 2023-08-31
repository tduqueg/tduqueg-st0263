# info de la materia: ST0263 <Nombre de la Materia>

Estudiante(s): Tomás Duque Giraldo, tduqueg@eafit.edu.co

Profesor: Edwin Montoya

# Sistema de Microservicios con RabbitMQ

1. **Breve Descripción de la Actividad**

Este proyecto implementa un sistema de microservicios con RabbitMQ. A través de una interfaz API principal, los usuarios pueden solicitar listas de archivos y realizar búsquedas por nombre. Estas solicitudes se manejan en microservicios que se comunican mediante RabbitMQ para la orquestación de tareas.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

- Implementación de una API con Express.
- Uso de microservicios para separar la lógica de listar y buscar archivos.
- Integración con RabbitMQ para gestionar las comunicaciones entre microservicios.
- Diseño modular y organizado.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

# 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

Se implementó una arquitectura de microservicios utilizando Express y gRPC para la comunicación. RabbitMQ se utiliza como mediador para la comunicación entre servicios. La estructura del proyecto está organizada modularmente, separando configuraciones, servicios y la lógica principal en diferentes carpetas y archivos.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

- Lenguaje: Nodejs
- Librerías:
  - express (version)
  - gRPC (version)
  - RabbitMQ (version)
  - Pika (version para RabbitMQ en nodejs)

## Cómo se compila y ejecuta.

1. Inicia RabbitMQ.

```bash
sudo docker start rabbit-server
```

2. Lanza los microservicios y la API principal.

3. Por medio de un buscador o postman colocar la dirección IP de la API y el puerto 80, luego colocar la ruta /list y se obtendrá la lista de archivos de la siguiente forma

```bash
http://<IP_DE_LA_API>:80/list
```

o si en su defecto deseas buscar un archivo en especifico se debe colocar la ruta /search y se debe colocar el nombre del archivo que se desea buscar de la siguiente forma

```bash
http://<IP_DE_LA_API>:80/search?name=<NOMBRE_DEL_ARCHIVO>
```

## Detalles técnicos

Las direcciones IP para los servicios son:

- API: 3.227.195.79
- MOM (RabbitMQ): 52.6.98.238
- gRPC: 54.237.135.137

los puertos de cada servicio son:
API: 80
MOM (RabbitMQ): 5672
gRPC: 50051

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

- Lenguaje: Nodejs
- Librerías:
  - express (version)
  - gRPC (version)
  - RabbitMQ (version)
  - Pika (version para RabbitMQ en nodejs)

## Cómo se compila y ejecuta.

1. Inicia RabbitMQ.

```bash
sudo docker start rabbit-server
```

2. Lanza los microservicios y la API principal.

## Detalles técnicos

Las direcciones IP para los servicios son:

- API: 3.227.195.79
- MOM (RabbitMQ): 52.6.98.238
- gRPC: 54.237.135.137

los puertos de cada servicio son:
API: 80
MOM (RabbitMQ): 5672
gRPC: 50051

# IP o nombres de dominio en nube o en la máquina servidor.

IPs:

- API: 3.227.195.79
- MOM (RabbitMQ): 52.6.98.238
- gRPC: 54.237.135.137

## Descripción y cómo se configura los parámetros del proyecto

Se debe configurar el archivo server.js con las direcciones IP de los servicios y además colocar los puertos que desee utilizar y las credenciales de RabbitMQ.

## Cómo se lanza el servidor.

1. Asegúrate de que RabbitMQ esté corriendo.
2. Lanza el API y el gRPC desde sus respectivos directorios.

# 5. Otra información que considere relevante para esta actividad.

N/A

# Referencias:

- RabbitMQ Official Documentation: https://www.rabbitmq.com/documentation.html

#### versión README.md -> 1.0 (2023-agosto)
