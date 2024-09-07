from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required

from sqlalchemy import Float
from flask_wtf import FlaskForm
import os
import pathlib

from app import db
from app.misc import format_currency_brl, gerar_sigla
from app.models import Processos
from app.Forms import SearchProc, ProcessoForm


path_templates = os.path.join(pathlib.Path(__file__).parent.resolve(),
                              "templates")

procs = Blueprint("procs", __name__,  template_folder=path_templates)

@procs.route("/processos", methods=["GET"])
@login_required
def processos():

    return redirect(url_for("procs.consulta"))


@procs.route("/processos/consulta", methods=["GET", "POST"])
@login_required
def consulta():

    title = "Processos"
    form = SearchProc()
    database = Processos.query.all()
    if form.validate_on_submit():

        coluna = getattr(Processos, form.tipoBusca.data)
        database = Processos.query.filter(coluna.contains(form.campo_busca.data)).all()

    page = "processos.html"
    return render_template("index.html", page=page, database=database, 
                           form=form, format_currency_brl=format_currency_brl,
                           title=title)


@procs.route("/processos/cadastro", methods=["GET", "POST"])
@login_required
def cadastro():

    page = "FormProc.html"
    form = ProcessoForm()

    func = "Cadastro"
    title = "Processos"
    
    error_messages = None
    
    action_url = url_for('procs.cadastro')
    
    if form.validate_on_submit():

        check_proc = Processos.query.filter_by(
            numproc=form.numproc.data).first()
        if not check_proc:

            data: dict[str, str] = {}
            for coluna in Processos.__table__.columns:

                info_data = form.data.get(coluna.name, None)
                if info_data:
                    
                    if isinstance(coluna.type, Float):
                        info_data = info_data.encode(
                            'latin-1', 'ignore').decode('latin-1')
                        info_data = float(info_data.replace(r"R$\xa", "").replace(
                            "R$ ", "").replace(".", "").replace(",", "."))

                    data.update({coluna.name: info_data})

            Processo = Processos(**data)
            db.session.add(Processo)
            db.session.commit()

            flash("Processo cadastrado com sucesso!", "success")
            return redirect(url_for("procs.consulta"))

        flash("Processo já cadastrado!", "error")
        return redirect(url_for("procs.consulta"))

    if form.errors:
        error_messages = []
        for message in form.errors:
            msg = form.errors[message]
            for mensagem in msg:
                error_messages.append((message, mensagem))
    
    return render_template("index.html", page=page, form=form,
                           title=title, func=func, 
                           action_url=action_url, error_messages=error_messages)


@procs.route("/processos/detalhes/<id>", methods=["GET"])
@login_required
def detalhes(id: int):

    page = "detalhes.html"
    return render_template("index.html", page=page)


@procs.route("/processos/editar/<id>", methods=["GET", "POST"])
@login_required
def editar(id: int):

    page = "FormProc.html"
    func = "Editar"
    title = "Processos"
    action_url = url_for('procs.editar', id=id)
    dbase = Processos.query.filter_by(id=id).first()
    error_messages = None
    
    data: dict[str, str] = {}
    for column in dbase.__table__.columns:
        
        form_field = getattr(ProcessoForm(), f"{column.name.lower()}", None)
        if form_field:
            set_data = getattr(dbase, column.name)
            if isinstance(column.type, Float):
                set_data = format_currency_brl(set_data)
            data.update({column.name: set_data})
    
    form = ProcessoForm(**data)
    
    if form.validate_on_submit():
        
        for column in dbase.__table__.columns:
            form_field = getattr(form, f"{column.name}", None)
            if form_field:
                
                data_insert = form_field.data
                if isinstance(column.type, Float):
                    data_insert = data_insert.encode(
                        'latin-1', 'ignore').decode('latin-1')
                    data_insert = float(data_insert.replace(r"R$\xa", "").replace(
                        "R$ ", "").replace(".", "").replace(",", "."))
                
                setattr(dbase, column.name, data_insert)
                
        db.session.commit()
        flash("Alterações salvas com sucesso!", "success")
        return redirect(url_for("procs.consulta"))
        
    if form.errors:
        error_messages = []
        for message in form.errors:
            msg = form.errors[message]
            for mensagem in msg:
                error_messages.append((message, mensagem))
    
    return render_template("index.html", page=page, form=form,
                           title=title, func=func, 
                           action_url=action_url, error_messages=error_messages)



@procs.route("/processos/desabilitar/<id>", methods=["POST"])
@login_required
def desabilitar():

    page = "desabilitar.html"
    return render_template("index.html", page=page)
