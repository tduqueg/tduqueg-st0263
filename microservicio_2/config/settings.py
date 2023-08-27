import os

# Aquí puedes poner la dirección IP pública de la instancia EC2
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', 5000))
# Directorio por defecto, puedes cambiarlo si es necesario
DIRECTORY = os.environ.get('DIRECTORY', './')
