from flask import Flask
from flask_restx import Api
from .api import api_namespace

def create_app():
    app = Flask(__name__)

    api = Api(
        app,
        version="1.0",
        title="HBnB API",
        description="HBnB Application API",
        prefix="/api"
    )

    api.add_namespace(api_namespace)

    return app
