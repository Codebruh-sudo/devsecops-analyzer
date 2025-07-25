from flask import Flask
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    Swagger(app)  # Initialize Swagger
    from .routes import bp
    app.register_blueprint(bp)
    return app
