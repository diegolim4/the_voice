from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS


from app.routes import route_about, route_import_ctrl

load_dotenv()

def run_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(route_about)
    app.register_blueprint(route_import_ctrl)

    return app

app = run_app()

if __name__ == '__main__':
    app.run()
