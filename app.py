from flask import Flask
import routes, models


def create_app(name):
    app = Flask(name)
    routes.register_routes(app)
    return app


app = create_app(__name__)