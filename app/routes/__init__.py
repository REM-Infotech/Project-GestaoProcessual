from flask import Flask
from flask import current_app as app
from flask import redirect, url_for

from .auth import auth
from .clientes import clients
from .dashboard import dash
from .index import index
from .partes import person
from .processos import procs


def register_blueprints(app: Flask):
    """
    Register a list of blueprints to the Flask application.
    Args:
        app (Flask): The Flask application instance to which the blueprints will be registered.
    Blueprints:
        auth: Blueprint for authentication routes.
        dash: Blueprint for dashboard routes.
        procs: Blueprint for process management routes.
        person: Blueprint for person-related routes.
        clients: Blueprint for client-related routes.
        index: Blueprint for index/home routes.
    """

    bps = [auth, dash, procs, person, clients, index]
    for blueprint in bps:
        app.register_blueprint(blueprint)


@app.route("/")
def redirect_login():

    return redirect(url_for("auth.login"))
