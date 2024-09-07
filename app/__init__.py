from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from app import default_config
from configs import csp

import os
import pathlib
from datetime import timedelta

src_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "src")
app = Flask(__name__, static_folder=src_path)
app.config.from_object(default_config)

db = SQLAlchemy()
tlsm = Talisman()
login_manager = LoginManager()

def init_app() -> None:
    
    from app.models import init_database
    age = timedelta(days=31).max.seconds
    db.init_app(app)
    login_manager.init_app(app)
    tlsm.init_app(app, content_security_policy=csp(),
                session_cookie_http_only=True,
                session_cookie_samesite='Lax',
                strict_transport_security=True,
                strict_transport_security_max_age=age,
                x_content_type_options= True,
                x_xss_protection=True)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = "Faça login para acessar essa página."
    login_manager.login_message_category = "info"
    init_database()
    
init_app()

from app import routes
# run_with_cloudflared(app)