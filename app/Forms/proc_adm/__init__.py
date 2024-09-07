from flask_wtf import FlaskForm
from wtforms import (StringField, DateField, SubmitField, 
                     SelectField, EmailField, BooleanField)
from wtforms.validators import DataRequired

import pytz
from datetime import datetime
from app.Forms.proc_adm.defaults import bairros_manaus, cidades_amazonas

import string
import random

from app.models import Partes


class SearchProc(FlaskForm):
    
    campo_busca = StringField("Buscar...")
    tipoBusca = SelectField("Buscar por: ", choices=[])
    
    def __init__(self, *args, **kwargs):
        
        super(SearchProc, self).__init__(*args, **kwargs)
        self.tipoBusca.choices = [
            ("numproc", "Número do Processo"),
            ("parte_contraria", "Parte Contrária"),
            ("cliente", "Cliente"),
            ("uc", "Unidade Consumidora"),
            ("bairro", "Bairro"),
            ("cidade", "Cidade"),
            ("estado", "Estado"),
        ]
        
    submit = SubmitField("Buscar")
    
class ProcessoForm(FlaskForm):
    
    numproc = StringField("Número do Processo *", validators=[DataRequired()])
    auto_import = BooleanField("Importar Automaticamente dados do Processo")
    cliente = SelectField("Cliente", choices=[("vazio", "Vazio")])
    parte_contraria = SelectField("Parte Contrária", choices=[("vazio", "Vazio")])
    adv_contrario = StringField("Advogado Parte Contrária")
    assunto = SelectField("Assunto", choices=[("vazio", "Vazio")])
    classe = SelectField("Classe", choices=[("vazio", "Vazio")])
    foro = SelectField("Foro", choices=[("vazio", "Vazio")])
    vara = SelectField("Vara", choices=[("vazio", "Vazio")])
    juiz = SelectField("Juiz", choices=[("vazio", "Vazio")])
    area = StringField("Área")
    valor_causa = StringField("Valor da Causa")
    data_distribuicao = DateField("Data Distribuição")
    data_cadastro = DateField("Data Cadastro", default=datetime.now(pytz.timezone('Etc/GMT+4')).date())
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super(ProcessoForm, self).__init__(*args, **kwargs)
        
        parte_contrariaes = [(Parte.nome, Parte.nome) for Parte in Partes.query.all()]
        if parte_contrariaes:
            self.parte_contraria.choices.extend(parte_contrariaes)

class PessoaForm(FlaskForm):
    
    nome = StringField("Nome *", validators=[DataRequired()])
    cpf_cnpj = StringField("CPF/CNPJ *", validators=[DataRequired()])
    endereco = StringField("Endereço")
    bairro = StringField("Bairro")
    cidade = StringField("Cidade")
    estado = StringField("Estado")
    cep = StringField("CEP")
    email = EmailField("E-mail")
    telefone1 = StringField("Telefone 1")
    telefone2 = StringField("Telefone 2")
    telefone3 = StringField("Telefone 3")
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)
    
class clienteForm(FlaskForm):
    
    cliente = StringField("Nome cliente *", validators=[DataRequired()])
    cpf_cnpj = StringField("CPF/CNPJ *", validators=[DataRequired()])
    endereco = StringField("Endereço")
    cidade = StringField("Cidade")
    estado = StringField("Estado")
    cep = StringField("CEP")
    email = StringField("E-mail")
    telefone1 = StringField("Telefone 1")
    telefone2 = StringField("Telefone 2")
    telefone3 = StringField("Telefone 3")
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super(clienteForm, self).__init__(*args, **kwargs)
