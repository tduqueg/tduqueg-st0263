import os


HOST = os.environ.get('HOST', '18.208.103.163')
PORT = int(os.environ.get('PORT', 5000))
# Directorio por defecto, puedes cambiarlo si es necesario
DIRECTORY = os.environ.get('DIRECTORY', './')
