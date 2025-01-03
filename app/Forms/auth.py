from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):

    login = StringField("Usuário", validators=[DataRequired("Informe o usuário!")])
    password = PasswordField("Senha", validators=[DataRequired("Informe a Senha!")])
    remember_me = BooleanField("Manter sessão")
    submit = SubmitField("Entrar")
