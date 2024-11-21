from flask import Flask
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    # Load environment variables from .env file
    load_dotenv()

    # Register Blueprints or Import routes directly
    from .routes import main as main_routes
    app.register_blueprint(main_routes)

    return app