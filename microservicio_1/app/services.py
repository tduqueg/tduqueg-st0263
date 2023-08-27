import os
from config.settings import DIRECTORY


def list_files():
    with os.scandir(DIRECTORY) as entries:
        files = [entry.name for entry in entries if entry.is_file()]
    return files
