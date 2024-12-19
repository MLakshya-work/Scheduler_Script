from flask import Flask
from app.routes import routes

def create_app():
    """
    Factory function to create and configure the Flask app.
    """
    app = Flask(__name__)

    # Register the Blueprint
    app.register_blueprint(routes)

    return app

