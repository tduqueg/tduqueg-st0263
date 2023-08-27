from flask import Blueprint, jsonify
from .services import search_files

bp = Blueprint('main', __name__)


@bp.route('/search/<pattern>', methods=['GET'])
def search_endpoint(pattern):
    files = search_files(pattern)
    return jsonify(files)
