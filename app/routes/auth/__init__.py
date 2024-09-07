from flask import (Blueprint, render_template, redirect, 
                   url_for, flash, session, request)
from app.Forms import LoginForm
from app.models import Users
import os
import pathlib

from flask_login import login_user, logout_user

path_templates = os.path.join(pathlib.Path(__file__).parent.resolve(),
                              "templates")
auth = Blueprint("auth", __name__, template_folder=path_templates)

@auth.route("/login", methods=["GET", "POST"])
def login():

    next_page = request.args.get("next")
    if next_page:
        session["location"] = next_page
        
    if not session.get("location", None):
        location = url_for("dash.dashboard")
        session["location"] = location
    
    form = LoginForm()
    if form.validate_on_submit():
        
        usuario = Users.query.filter(
            Users.login == form.login.data).first()
        
        if usuario:
            checkpw = usuario.converte_senha(form.password.data)
            if checkpw:
                
                session["nome_usuario"] = usuario.nome_usuario
                flash("Login efetuado com sucesso!")
                login_user(usuario, True)
                to_end = session["location"]
                session.pop("location")
                return redirect(to_end)
            
            flash("Senha Incorreta!", "error")
        
        if not usuario:
            flash("Usuário não encontrado!")

    return render_template("login.html", form=form)

@auth.route("/logout", methods = ["GET"])
def logout():
    
    logout_user()
    flash("Sessão encerrada!")
    return redirect(url_for("auth.login"))
