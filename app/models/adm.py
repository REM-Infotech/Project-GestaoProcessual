from datetime import datetime
from app import db
import pytz

class ProcsADM(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    numproc = db.Column(db.String(length=64), nullable=False)
    devedor = db.Column(db.String(length=64), nullable=False)
    empresa = db.Column(db.String(length=64), nullable=False)
    uc_contrato = db.Column(db.String(length=64), nullable=False)
    endereco_debto = db.Column(db.String(length=64), nullable=False)
    bairro = db.Column(db.String(length=64), nullable=False)
    cidade = db.Column(db.String(length=64), nullable=False)
    estado = db.Column(db.String(length=64), nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Etc/GMT+4')))
    

class Debitos(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    procadm = db.Column(db.String(length=64), nullable=False)
    uc = db.Column(db.String(length=64), nullable=False)
    devedor = db.Column(db.String(length=64), nullable=False)
    mes_ref = db.Column(db.String(length=64), nullable=False)
    valor_debito = db.Column(db.Float, nullable=False)
    
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
    
class Bairros(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    bairro = db.Column(db.String(length=64), nullable=False)
    
class Cidades(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    cidade = db.Column(db.String(length=64), nullable=False)
    
class Estados(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    estado = db.Column(db.String(length=64), nullable=False)

class Empresas(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    empresa = db.Column(db.String(length=64), nullable=False)
    cnpj = db.Column(db.String(length=64), nullable=False)
    endereco = db.Column(db.String(length=64))
    cidade = db.Column(db.String(length=64))
    estado = db.Column(db.String(length=64))
    cep = db.Column(db.String(length=64))
    email = db.Column(db.String(length=64))
    telefone1 = db.Column(db.String(length=64))
    telefone2 = db.Column(db.String(length=64))
    telefone3 = db.Column(db.String(length=64))
