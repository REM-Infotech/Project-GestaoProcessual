from flask import Flask, redirect, url_for, current_app as app

from app.routes.auth import auth
from app.routes.dashboard import dash
from app.routes.processos import procs
from app.routes.partes import person
from app.routes.clientes import clients


def register_blueprints(app: Flask):

    bps = [auth, dash, procs, person, clients]
    for blueprint in bps:
        app.register_blueprint(blueprint)


@app.route("/")
def index():

    return redirect(url_for("auth.login"))
