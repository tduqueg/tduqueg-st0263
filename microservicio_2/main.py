from flask import Flask
from app import create_app
from app.routes import bp as main_bp
from config.settings import HOST, PORT


app = create_app()
app.register_blueprint(main_bp)

if __name__ == '__main__':

    app.run(host=HOST, port=PORT)
