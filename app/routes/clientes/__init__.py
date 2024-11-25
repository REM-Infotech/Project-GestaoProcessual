from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
import os
import pathlib

from app import db
from app.models import Clientes
from app.Forms import clienteForm
from app.misc import formatar_numero

path_templates = os.path.join(pathlib.Path(__file__).parent.resolve(), "templates")
clients = Blueprint("clients", __name__, template_folder=path_templates)


@clients.route("/clientes", methods=["GET"])
@login_required
def index():

    return redirect(url_for("clients.consulta"))


@clients.route("/clientes/consulta", methods=["GET", "POST"])
@login_required
def consulta():

    title = "Clientes"
    page = "clientes.html"

    database = Clientes.query.all()

    return render_template("index.html", page=page, title=title, database=database)


@clients.route("/clientes/cadastro", methods=["GET", "POST"])
@login_required
def cadastro():

    title = "Clientes"
    func = "Cadastro"
    page = "Formclientes.html"
    url_action = url_for("clients.cadastro")
    form = clienteForm()

    if form.validate_on_submit():

        check_cliente = Clientes.query.filter(
            Clientes.cpf_cnpj == form.cpf_cnpj.data
        ).first()

        if not check_cliente:

            data: dict[str, str] = {}
            for coluna in Clientes.__table__.columns:

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

            cliente = Clientes(**data)
            db.session.add(cliente)
            db.session.commit()

            flash("cliente cadastrada com sucesso!", "success")
            return redirect(url_for("clients.consulta"))

        flash("cliente já cadastrada!", "error")

    return render_template(
        "index.html",
        page=page,
        title=title,
        func=func,
        url_action=url_action,
        form=form,
    )


@clients.route("/clientes/editar/<id>", methods=["GET", "POST"])
@login_required
def editar(id: int):

    title = "Clientes"
    func = "Editar"
    page = "Formclientes.html"
    url_action = url_for("clients.editar", id=id)

    dbase = Clientes.query.filter(Clientes.id == id).first()

    data: dict[str, str] = {}
    for column in dbase.__table__.columns:

        form_field = getattr(clienteForm(), f"{column.name.lower()}", None)
        if form_field:
            set_data = getattr(dbase, column.name)
            data.update({column.name: set_data})

    form = clienteForm(**data)
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
        return redirect(url_for("clients.consulta"))

    return render_template(
        "index.html",
        page=page,
        title=title,
        func=func,
        url_action=url_action,
        form=form,
    )
