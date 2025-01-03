from datetime import datetime

import pytz

from app import db


class Processos(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    numproc = db.Column(db.String(length=64), nullable=False, unique=True)
    parte_contraria = db.Column(db.String(length=64), nullable=False)
    adv_contrario = db.Column(db.String(length=64), nullable=False)
    cliente = db.Column(db.String(length=64), nullable=False)
    assunto = db.Column(db.String(length=64), nullable=False)
    classe = db.Column(db.String(length=64), nullable=False)
    foro = db.Column(db.String(length=64), nullable=False)
    vara = db.Column(db.String(length=64), nullable=False)
    juiz = db.Column(db.String(length=64), nullable=False)
    area = db.Column(db.String(length=64), nullable=False, default="Vazio")
    valor_causa = db.Column(db.Float, nullable=False, default=0.01)
    data_distribuicao = db.Column(
        db.DateTime, default=datetime.now(pytz.timezone("Etc/GMT+4"))
    )
    data_cadastro = db.Column(
        db.DateTime, default=datetime.now(pytz.timezone("Etc/GMT+4"))
    )


class Partes(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    nome = db.Column(db.String(length=64), nullable=False)
    cpf_cnpj = db.Column(db.String(length=64))
    endereco = db.Column(db.String(length=64))
    bairro = db.Column(db.String(length=64))
    cidade = db.Column(db.String(length=64))
    estado = db.Column(db.String(length=64))
    cep = db.Column(db.String(length=64))
    email = db.Column(db.String(length=64))
    telefone1 = db.Column(db.String(length=64))
    telefone2 = db.Column(db.String(length=64))
    telefone3 = db.Column(db.String(length=64))


class Assuntos(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    assunto = db.Column(db.String(length=64), nullable=False)


class Classes(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    classe = db.Column(db.String(length=64), nullable=False)


class Foros(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    foro = db.Column(db.String(length=64), nullable=False)


class Varas(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    vara = db.Column(db.String(length=64), nullable=False)


class Juizes(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    juiz = db.Column(db.String(length=64), nullable=False)


class Clientes(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    cliente = db.Column(db.String(length=64), nullable=False)
    cpf_cnpj = db.Column(db.String(length=64), nullable=False)
    endereco = db.Column(db.String(length=64))
    cidade = db.Column(db.String(length=64))
    estado = db.Column(db.String(length=64))
    cep = db.Column(db.String(length=64))
    email = db.Column(db.String(length=64))
    telefone1 = db.Column(db.String(length=64))
    telefone2 = db.Column(db.String(length=64))
    telefone3 = db.Column(db.String(length=64))
