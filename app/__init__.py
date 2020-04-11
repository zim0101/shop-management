from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand


# Globally accessible libraries
db = SQLAlchemy()
marshmallow = Marshmallow()
bcrypt = Bcrypt()
migrate = Migrate()


def create_app():
    # Initialize the core application
    app = Flask(__name__, instance_relative_config=False)

    # Dynamic configuration
    if app.config['ENV'] == 'development':
        app.config.from_object('config.Development')
    if app.config['ENV'] == 'production':
        app.config.from_object('config.Production')
    if app.config['ENV'] == 'testing':
        app.config.from_object('config.Testing')

    # Initialize Plugins
    db.init_app(app)
    marshmallow.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Import views
        from . import views
        from product.views import product
        from user import auth

        # Import models
        from product.models import Product
        from user.models import User
        from category.models import Category, Subcategory
        from employee.models import Employee

        db.create_all()

        # Register Blueprints
        app.register_blueprint(product, url_prefix='/product')

        return app
