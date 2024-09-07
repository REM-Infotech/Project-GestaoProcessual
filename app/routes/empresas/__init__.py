from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
import os
import pathlib

from app import db
from app.models import Empresas
from app.Forms import EmpresaForm
from app.misc import formatar_numero

path_templates = os.path.join(pathlib.Path(__file__).parent.resolve(), 
                              "templates")
company = Blueprint("company", __name__,  template_folder=path_templates)

@company.route("/empresas", methods = ["GET"])
@login_required
def index():
    
    return redirect(url_for("company.consulta"))

@company.route("/empresas/consulta", methods = ["GET", "POST"])
@login_required
def consulta():
    
    title = "Empresas"
    page = "empresas.html"
    
    database = Empresas.query.all()
    
    return render_template("index.html", page=page, 
                           title=title, database=database)

@company.route("/empresas/cadastro", methods = ["GET", "POST"])
@login_required
def cadastro():
    
    title = "Empresas"
    func = "Cadastro"
    page = "Formempresas.html"
    url_action = url_for("company.cadastro")
    form = EmpresaForm()
    
    if form.validate_on_submit():

        check_Empresa = Empresas.query.filter(
            Empresas.cnpj == form.cnpj.data).first()
        
        if not check_Empresa:

            data: dict[str, str] = {}
            for coluna in Empresas.__table__.columns:

                form_field = getattr(form, f"{coluna.name.lower()}", None)
                if form_field:
                    data_insert = form_field.data
                    if not data_insert:
                        continue
                    
                    if "telefone" in coluna.name:
                        data_insert = formatar_numero(data_insert)
                        if not data_insert:
                            flash("Informe o DDI do telefone!", "error") 
                            return redirect(url_action)
                        
                    data.update({coluna.name: data_insert})
                    
            Empresa = Empresas(**data)
            db.session.add(Empresa)
            db.session.commit()

            flash("Empresa cadastrada com sucesso!", "success")
            return redirect(url_for("company.consulta"))

        flash("Empresa já cadastrada!", "error")
    
    return render_template("index.html", page=page, title=title, 
                           func=func, url_action=url_action, form=form)

@company.route("/empresas/editar/<id>", methods = ["GET", "POST"])
@login_required
def editar(id: int):
    
    title = "Empresas"
    func = "Editar"
    page = "Formempresas.html"
    url_action = url_for("company.editar", id=id)
    
    dbase = Empresas.query.filter(Empresas.id == id).first()
    
    data: dict[str, str] = {}
    for column in dbase.__table__.columns:
        
        form_field = getattr(EmpresaForm(), f"{column.name.lower()}", None)
        if form_field:
            set_data = getattr(dbase, column.name)
            data.update({column.name: set_data})
    
    form = EmpresaForm(**data)
    if form.validate_on_submit():
        
        for column in dbase.__table__.columns:
            form_field = getattr(form, f"{column.name}", None)
            if form_field:
                data_insert = form_field.data
                if not data_insert:
                    continue
                
                if "telefone" in column.name:
                    data_insert = formatar_numero(data_insert)
                    if not data_insert:
                        flash("Informe o DDI do telefone!", "error") 
                        return redirect(url_action)
                    
                setattr(dbase, column.name, data_insert)
                
        db.session.commit()
        flash("Alterações salvas com sucesso!", "success")
        return redirect(url_for("company.consulta"))
    
    return render_template("index.html", page=page, title=title, 
                           func=func, url_action=url_action, form=form)