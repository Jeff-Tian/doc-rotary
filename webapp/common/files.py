# common/files.py
import os
from common.config import cfg as config
from werkzeug.utils import secure_filename


def uploads_url(path):
    return path.replace(config['uploads_dir'], '/uploads')


def save_to(folder, file):
    os.makedirs(folder, exist_ok=True)
    save_path = os.path.join(folder, secure_filename(file.filename))
    file.save(save_path)
    return save_path
