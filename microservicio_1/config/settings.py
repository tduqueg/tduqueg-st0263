import os

HOST = os.environ.get('HOST', '0.0.0.0')# Hay que cambiarlo por la ip de la instancia
PORT = int(os.environ.get('PORT', 5000))
DIRECTORY = os.environ.get('DIRECTORY', './')  
