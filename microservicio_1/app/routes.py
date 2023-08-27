from flask import Blueprint, jsonify
from .services import list_files

bp = Blueprint('main', __name__)


@bp.route('/list', methods=['GET'])
def list_endpoint():
    files = list_files()
    return jsonify(files)
