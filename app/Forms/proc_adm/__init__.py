from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectField, EmailField
from wtforms.validators import DataRequired

import pytz
from datetime import datetime
from app.Forms.proc_adm.defaults import bairros_manaus, cidades_amazonas

import string
import random

from app.models import ProcsADM, Bairros, Cidades, Estados, Empresas, Partes


class SearchProc(FlaskForm):
    
    campo_busca = StringField("Buscar...")
    tipoBusca = SelectField("Buscar por: ", choices=[])
    
    def __init__(self, *args, **kwargs):
        
        super(SearchProc, self).__init__(*args, **kwargs)
        self.tipoBusca.choices = [
            ("numproc", "Número do Processo"),
            ("devedor", "Devedor"),
            ("empresa", "Empresa"),
            ("uc", "Unidade Consumidora"),
            ("bairro", "Bairro"),
            ("cidade", "Cidade"),
            ("estado", "Estado"),
        ]
        
    submit = SubmitField("Buscar")
    
class ProcessoForm(FlaskForm):
    
    numproc = StringField("Número do Processo", validators=[DataRequired()])
    devedor = SelectField("Devedor", choices=[])
    empresa = SelectField("Empresa", choices=[])
    uc_contrato = StringField("Unidade Consumidora / Contrato")
    endereco_debto = StringField("Endereço Débito")
    bairro = SelectField("Bairro", choices=bairros_manaus)
    cidade = SelectField("Cidade", choices=[])
    estado = SelectField("Estado", choices=[("Amazonas", "Amazonas")])
    valor_total = StringField("Valor total débitos")
    data_cadastro = DateField("Data Cadastro", default=datetime.now(pytz.timezone('Etc/GMT+4')).date())
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super(ProcessoForm, self).__init__(*args, **kwargs)

        numproc = kwargs.get("numproc", None)
        while not numproc:
            
            check_num = ProcsADM.query.filter_by(numproc=numproc).first()
            if not check_num:
                numproc = f"{''.join(random.choices(string.digits, k=6))}"
        
        self.numproc.data = numproc
        self.bairro.choices.extend(bairros_manaus)
        self.cidade.choices.extend(cidades_amazonas)
        
        empresa = [(Empresa.empresa, Empresa.empresa) for Empresa in Empresas.query.all()]
        self.empresa.choices.extend(empresa)
        
        devedores = [(Parte.nome, Parte.nome) for Parte in Partes.query.all()]
        if devedores:
            self.devedor.choices.extend(devedores)
        
        # self.estado.choices.extend([(Estados.estado, Estados.estado) for Estados in Estados.query.all()])

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
    
class EmpresaForm(FlaskForm):
    
    empresa = StringField("Nome Empresa *", validators=[DataRequired()])
    cnpj = StringField("CNPJ *", validators=[DataRequired()])
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
        super(EmpresaForm, self).__init__(*args, **kwargs)
