from flask import Blueprint

from app.controller.import_controller import insert_voice_controller

route_about = Blueprint('about', __name__)
route_import_ctrl = Blueprint('import_voice', __name__)

@route_about.route('/api/about')    
def about():
    return 'The Voice ok! 😎'

@route_import_ctrl.route('/api/import_voice', methods=['POST'])
def insert_voice_router():
    return insert_voice_controller()

