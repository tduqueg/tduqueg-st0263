# info de la materia: STxxxx <Nombre de la Materia>

Estudiante(s): Tomás Duque Giraldo, tduqueg@eafit.edu.co

Profesor: Edwin Montoya

# Sistema de Microservicios con RabbitMQ

1. **Breve Descripción de la Actividad**

Este proyecto implementa un sistema de microservicios con RabbitMQ. A través de una interfaz API principal, los usuarios pueden solicitar listas de archivos y realizar búsquedas por nombre. Estas solicitudes se manejan en microservicios que se comunican mediante RabbitMQ para la orquestación de tareas.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

- Implementación de una API con Flask.
- Uso de microservicios para separar la lógica de listar y buscar archivos.
- Integración con RabbitMQ para gestionar las comunicaciones entre microservicios.
- Diseño modular y organizado.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

# 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

Se implementó una arquitectura de microservicios utilizando Flask y gRPC para la comunicación. RabbitMQ se utiliza como mediador para la comunicación entre servicios. La estructura del proyecto está organizada modularmente, separando configuraciones, servicios y la lógica principal en diferentes carpetas y archivos.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

- Lenguaje: Python 3.9
- Librerías:
  - Flask (version)
  - gRPC (version)
  - RabbitMQ (version)
  - Pika (version para RabbitMQ en Python)

## Cómo se compila y ejecuta.

1. Instala las dependencias usando pip:

```bash
pip install -r requirements.txt
```

2. Inicia RabbitMQ.

3. Lanza los microservicios y la API principal.

## Detalles técnicos

Las direcciones IP para los servicios son:

- microservicio1: 3.227.195.79
- microservicio2: 18.208.103.163
- MOM (RabbitMQ): 52.6.98.238
- gRPC: 54.237.135.137

La configuración, como IPs y puertos, se encuentra en el archivo de configuración dentro de cada componente.

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

<Replica lo que se mencionó en la sección 3 si el ambiente de producción es similar al de desarrollo>

# IP o nombres de dominio en nube o en la máquina servidor.

IPs:

- microservicio1: 3.227.195.79
- microservicio2: 18.208.103.163
- MOM (RabbitMQ): 52.6.98.238
- gRPC: 54.237.135.137

## Descripción y cómo se configura los parámetros del proyecto

La configuración de cada microservicio y de la API principal se encuentra en archivos de configuración dentro de sus respectivas carpetas. Aquí se pueden ajustar IPs, puertos y otros parámetros relevantes.

## Cómo se lanza el servidor.

1. Asegúrate de que RabbitMQ esté corriendo.
2. Lanza cada microservicio y la API principal desde sus respectivos directorios.

# 5. Otra información que considere relevante para esta actividad.

N/A

# Referencias:

- RabbitMQ Official Documentation: https://www.rabbitmq.com/documentation.html
- Flask Documentation: https://flask.palletsprojects.com/en/2.0.x/
- gRPC Python Documentation: https://grpc.io/docs/languages/python/

#### versión README.md -> 1.0 (2023-agosto)
