import os
from flask import Flask
from app.extensions import db
from app.routes.routes import main

def create_app():
    app = Flask(__name__)

    # Configuration
    # Render sets the DATABASE_URL environment variable. 
    # We enforce PostgreSQL for both local and production environments.
    # Default to a local PostgreSQL instance if DATABASE_URL is not set.
    database_url = os.environ.get('DATABASE_URL', 'postgresql://postgres:database@localhost:5432/flask_db')
    
    # Fix for SQLAlchemy: Render uses postgres://, SQLAlchemy needs postgresql://
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_secret_key')

    # Initialize Extensions
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(main)

    return app