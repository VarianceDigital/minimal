import os

from flask import Flask
from .jinjafilters import *
from .errorhandlers import *

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ['SESSION_SECRET'],
    )

    from . import bl_home
    app.register_blueprint(bl_home.bp)

    from . import bl_modals
    app.register_blueprint(bl_modals.bp)

    from . import bl_niceurls
    app.register_blueprint(bl_niceurls.bp)

    #Add other blueprints if needed

    from . import auth
    app.register_blueprint(auth.bp)

    #ADDS HANDLER FOR ERRORs
    app.register_error_handler(500, error_500)
    app.register_error_handler(404, error_404)

    #JINJA FILTERS
    app.jinja_env.filters['slugify'] = slugify
    app.jinja_env.filters['displayError'] = displayError 
    app.jinja_env.filters['displayMessage'] = displayMessage

    return app