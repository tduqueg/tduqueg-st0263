import os
from config.settings import DIRECTORY
from .message_service import publish_message


def list_files():
    with os.scandir(DIRECTORY) as entries:
        files = [entry.name for entry in entries if entry.is_file()]
    return files


def add_file(filename, file_content):
    # Salvar el archivo a la ubicación.
    file_path = os.path.join(DIRECTORY, filename)
    with open(file_path, 'w') as f:
        f.write(file_content)

    # Notificar a través de RabbitMQ
    publish_message('files.new', filename)
