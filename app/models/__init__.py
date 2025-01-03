from uuid import uuid4

from dotenv import dotenv_values
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .adm import Assuntos, Classes, Clientes, Foros, Juizes, Partes, Processos, Varas
from .secondaries import admins
from .users import LicensesUsers, SuperUser, Users

__all__ = [
    admins,
    Users,
    LicensesUsers,
    SuperUser,
    Assuntos,
    Classes,
    Clientes,
    Foros,
    Juizes,
    Partes,
    Varas,
    Processos,
]


def init_database(app: Flask, db: SQLAlchemy) -> str:

    try:
        values = dotenv_values()
        db.create_all()
        loginsys = values.get("loginsys")
        nomeusr = values.get("nomeusr")
        emailusr = values.get("emailusr")
        passwd = values.get("passwd", str(uuid4()))

        dbase = Users.query.filter(Users.login == loginsys).first()
        if not dbase:

            user = Users(login=loginsys, nome_usuario=nomeusr, email=emailusr)
            user.senhacrip = passwd

            license_user = LicensesUsers.query.filter(
                LicensesUsers.name_client == "Robotz Dev"
            ).first()

            if not license_user:

                license_user = LicensesUsers(
                    name_client="Robotz Dev",
                    cpf_cnpj="55607848000175",
                    license_token=str(uuid4()),
                )

            user.licenseusr = license_user
            license_user.admins.append(user)
            super_user = SuperUser()

            super_user.users = user

            db.session.add(user)
            db.session.add(license_user)
            db.session.commit()

            return f" * Root Pw: {passwd}"

    except Exception as e:
        raise e
