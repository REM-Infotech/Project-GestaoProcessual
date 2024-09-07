from flask import redirect, url_for
from app import app

from app.routes.auth import auth
from app.routes.dashboard import dash
from app.routes.processos import procs
from app.routes.partes import person
from app.routes.empresas import company

app.register_blueprint(person)
app.register_blueprint(procs)
app.register_blueprint(auth)
app.register_blueprint(dash)
app.register_blueprint(company)

@app.route("/")
def index():
    
    return redirect(url_for("auth.login"))
