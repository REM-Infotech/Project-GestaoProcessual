from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
import os
import pathlib

from app import db
from typing import Type
from app.models import Partes
from app.Forms import PessoaForm
from app.misc import formatar_numero


path_templates = os.path.join(pathlib.Path(__file__).parent.resolve(), "templates")
person = Blueprint("person", __name__, template_folder=path_templates)


@person.route("/pessoas", methods=["GET"])
@login_required
def index():

    return redirect(url_for("person.consulta"))


@person.route("/pessoas/consulta", methods=["GET", "POST"])
@login_required
def consulta():

    title = "Pessoas"
    page = "pessoas.html"

    database = Partes.query.all()

    return render_template("index.html", page=page, title=title, database=database)


@person.route("/pessoas/cadastro", methods=["GET", "POST"])
@login_required
def cadastro():

    title = "Pessoas"
    func = "Cadastro"
    page = "FormPessoas.html"
    url_action = url_for("person.cadastro")
    form: Type[PessoaForm] = PessoaForm()

    if form.validate_on_submit():

        check_parte = Partes.query.filter(Partes.cpf_cnpj == form.cpf_cnpj.data).first()

        if not check_parte:

            data: dict[str, str] = {}
            for coluna in Partes.__table__.columns:

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

            Parte = Partes(**data)
            db.session.add(Parte)
            db.session.commit()

            flash("Parte cadastrada com sucesso!", "success")
            return redirect(url_for("person.consulta"))

        flash("Parte já cadastrada!", "error")

    return render_template(
        "index.html",
        page=page,
        title=title,
        func=func,
        url_action=url_action,
        form=form,
    )


@person.route("/pessoas/editar/<id>", methods=["GET", "POST"])
@login_required
def editar(id: int):

    title = "Pessoas"
    func = "Editar"
    page = "FormPessoas.html"
    url_action = url_for("person.editar", id=id)

    dbase = Partes.query.filter(Partes.id == id).first()

    data: dict[str, str] = {}
    for column in dbase.__table__.columns:

        form_field = getattr(PessoaForm(), f"{column.name.lower()}", None)
        if form_field:
            set_data = getattr(dbase, column.name)
            data.update({column.name: set_data})

    form = PessoaForm(**data)
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
        return redirect(url_for("person.consulta"))

    return render_template(
        "index.html",
        page=page,
        title=title,
        func=func,
        url_action=url_action,
        form=form,
    )
