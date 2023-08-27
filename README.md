# Proyecto Telemática: Microservicios con MOM

## Descripción

Este proyecto integra un conjunto de microservicios que tienen como función principal listar y buscar archivos dentro de directorios específicos. Se utiliza RabbitMQ como Middleware Orientado a Mensajes (MOM) para permitir la comunicación entre los servicios.

## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Funcionamiento](#funcionamiento)
- [Pre-requisitos](#pre-requisitos)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Notas Adicionales](#notas-adicionales)

## Estructura del Proyecto

### Carpetas y Archivos

#### `api`

Contiene el servidor principal que se encarga de gestionar las peticiones y comunicarse con los microservicios.

- `app.py`: Archivo que define las rutas y maneja la comunicación con los microservicios.

#### `microservicio_1`

Se encarga de listar los archivos de un directorio determinado.

- `main.py`: Punto de entrada del microservicio.
- `app/`
  - `services.py`: Funciones que facilitan la lista de archivos.

#### `microservicio_2`

Este microservicio tiene la capacidad de listar archivos y además buscarlos basados en un patrón dado.

- `main.py`: Punto de entrada y donde se inicia el listener de RabbitMQ.
- `app/`
  - `services.py`: Funciones para listar y buscar archivos.

#### `mom`

Conjunto de lógicas relacionadas con la interacción de RabbitMQ.

- `message_service.py`: Funciones para la publicación y escucha de mensajes usando RabbitMQ.

## Funcionamiento

1. El servidor principal (`api`) hace solicitudes para listar o buscar archivos.
2. Para buscar archivos, `api` publica un mensaje en RabbitMQ con el patrón de búsqueda deseado.
3. `microservicio_2`, que actúa como un listener de RabbitMQ, detecta este mensaje, realiza la búsqueda y responde con los archivos correspondientes.

## Pre-requisitos

- Tener instalado Python 3.x.
- RabbitMQ debe estar instalado y en funcionamiento.

## Instalación y Ejecución

1. Asegúrate que RabbitMQ esté corriendo en tu sistema.
2. Instala las dependencias con:
   ```bash
   pip install -r requirements.txt
   ```
3. inicia el `microservicio_1`:
   ```bash
   cd microservicio_1
   python main.py
   ```
4. inicia el `microservicio_2`:
   ```bash
   cd microservicio_2
   python main.py
   ```
5. finalmente, inicia el servidor principal:
   ```bash
   cd api
   python app.py
   ```

# Notas Adicionales

- Las configuraciones como la dirección IP, puertos de microservicios y RabbitMQ, entre otros, se encuentran en el archivo `config.py` de cada microservicio.
- Si se va a desplegar en diferentes máquinas asegurese que las direcciones IP y puertos estén configurados correctamente.
