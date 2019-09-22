import os
# import sys
from flask import Flask
# from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS

# instantiate the ap
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
cors = CORS()


def create_app(script_info=None):
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    # print(app.config, file=sys.stderr)

    db.init_app(app)
    toolbar.init_app(app)
    cors.init_app(app)

    # register blueprint
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
