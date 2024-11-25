import os
from datetime import timedelta
from pathlib import Path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman

from app import default_config
from configs import csp

db = None
login_manager = None


class AppFactory:

    def init_extensions(self, app: Flask) -> None:

        global db, login_manager
        db = SQLAlchemy()
        tlsm = Talisman()
        login_manager = LoginManager()

        db.init_app(app)
        login_manager.init_app(app)

        tlsm.init_app(
            app,
            content_security_policy=csp(),
            session_cookie_http_only=True,
            session_cookie_samesite="Lax",
            strict_transport_security=True,
            strict_transport_security_max_age=timedelta(days=31).max.seconds,
            x_content_type_options=True,
            x_xss_protection=True,
        )
        login_manager.login_view = "auth.login"
        login_manager.login_message = "Faça login para acessar essa página."
        login_manager.login_message_category = "info"

        with app.app_context():

            from .models import init_database

            is_init = Path(os.path.join(Path(__file__).parent.resolve(), "is_init.txt"))
            if not is_init.exists():
                with is_init.open("w") as f:
                    f.write(init_database(app, db))

    def create_app(self) -> Flask:

        src_path = os.path.join(Path(__file__).parent.resolve(), "src")
        app = Flask(__name__, static_folder=src_path)
        app.config.from_object(default_config)

        self.init_extensions(app)

        with app.app_context():
            from .routes import register_blueprints

            register_blueprints(app)

        return app


create_app = AppFactory().create_app
