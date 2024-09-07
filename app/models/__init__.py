
from app.models.adm import (ProcsADM, Debitos, Empresas, Estados, Partes, Bairros, Cidades)
from app.models.users import Users, Group, Permission

import os
import json
from uuid import uuid4
from app import app, db


def init_database():
    
    with app.app_context():
        
        db.create_all()
        
        usr = Users.query.filter_by(login="root").first()

        if usr is None:
            
            filename = "favicon.ico"
            path_img = os.path.join("app/src/assets/img", filename)
            with open(path_img, 'rb') as file:
                blob_doc = file.read()
            usr = Users(
                login="root",
                nome_usuario="Root",
                email="adm@robotz.dev",
                blob_doc = blob_doc,
                filename = filename)
            
            root_pw = str(uuid4())
            usr.senhacrip = root_pw
            print(f" * Root Pw: {root_pw}")
            
        db.session.add(usr)
        db.session.commit()