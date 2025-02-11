from flask import Flask

from .config import DefaultConfig
from .extensions import db

from .views import views

BLUEPRINTS = [views]

def create_app():
    app = Flask(__name__)

    configure_app(app)
    configure_extension(app)
    configure_blueprints(app, BLUEPRINTS)
    
    
    return app


def configure_app(app):
    app.config.from_object(DefaultConfig)


def configure_extension(app):
    db.init_app(app)

def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
