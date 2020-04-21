from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


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

    # Import models
    from auth import models
    from product.models import product, category, subcategory
    from shop.models import shop, shop_category

    # Initialize Plugins
    db.init_app(app)
    marshmallow.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Import views
        from . import views
        from auth.auth import auth
        from product.views.product_views import product
        from shop.views.shop_view import shop

        # Register Blueprints
        app.register_blueprint(auth, url_prefix='/api/auth')
        app.register_blueprint(product, url_prefix='/api/product')
        app.register_blueprint(shop, url_prefix='/api/shop')

        return app
