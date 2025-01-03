import secrets
from datetime import timedelta
from pathlib import Path

from dotenv import dotenv_values


class Config(object):

    DEBUG: bool = False
    TESTING: bool = False
    SECRET_KEY: str = secrets.token_hex()

    # FLASK-MAIL CONFIG
    MAIL_SERVER: str = ""
    MAIL_PORT = 587
    MAIL_USE_TLS: bool = False
    MAIL_USE_SSL: bool = False
    MAIL_USERNAME: str = ""
    MAIL_PASSWORD: str = ""
    MAIL_DEFAULT_SENDER: str = ""

    # SQLALCHEMY CONFIG
    SQLALCHEMY_POOL_SIZE = 30  # Número de conexões na pool
    SQLALCHEMY_MAX_OVERFLOW = 10  # Número de conexões extras além da pool_size
    SQLALCHEMY_POOL_TIMEOUT = 30  # Tempo de espera para obter uma conexão

    # Tempo (em segundos) para reciclar as conexões ociosas
    SQLALCHEMY_POOL_RECYCLE = 1800

    # Verificar a saúde da conexão antes de usá-la
    SQLALCHEMY_POOL_PRE_PING = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///local.db"
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # FLASK CONFIG
    PREFERRED_URL_SCHEME = "https"
    SESSION_COOKIE_HTTPONLY = False
    SESSION_COOKIE_SECURE = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=31).max.seconds

    TEMP_PATH = Path(__file__).cwd().joinpath("temp")
    TEMP_PATH.mkdir(exist_ok=True)

    CSP = {
        "default-src": ["'self'"],
        "script-src": [
            "'self'",
            "https://cdn.jsdelivr.net",
            "https://cdnjs.cloudflare.com",
            "https://cdn.datatables.net",
            "https://unpkg.com",
            "https://code.jquery.com",
            "https://use.fontawesome.com",
            "",
            "'unsafe-inline'",
        ],
        "style-src": [
            "'self'",
            "https://cdn.jsdelivr.net",
            "https://cdnjs.cloudflare.com",
            "https://cdn.datatables.net",
            "https://unpkg.com",
            "https://github.com",
            "https://avatars.githubusercontent.com",
            "'unsafe-inline'",
        ],
        "img-src": [
            "'self'",
            "data:",
            "https://cdn.jsdelivr.net",
            "https://cdnjs.cloudflare.com",
            "https://cdn.datatables.net",
            "https://unpkg.com",
            "https://cdn-icons-png.flaticon.com",
            "https://github.com",
            "https://domain.cliente.com",
            "https://avatars.githubusercontent.com",
            "https://cdn-icons-png.freepik.com",
        ],
        "connect-src": [
            "'self'",
            "https://cdn.jsdelivr.net",
            "https://cdnjs.cloudflare.com",
            "https://cdn.datatables.net",
            "https://github.com",
            "https://unpkg.com",
            "https://avatars.githubusercontent.com",
        ],
        "frame-src": [
            "'self'",
            "https://domain.cliente.com",
            "https://github.com",
            "https://avatars.githubusercontent.com",
        ],
    }


class ProductionConfig(Config):

    try:
        env = dotenv_values(".env")

        # Flask-mail config
        MAIL_SERVER = env["MAIL_SERVER"]
        MAIL_PORT = int(env["MAIL_PORT"])
        MAIL_USE_TLS = env["MAIL_USE_TLS"] in ["True", "true", "TRUE"]
        MAIL_USE_SSL = env["MAIL_USE_SSL"] in ["True", "true", "TRUE"]
        MAIL_USERNAME = env["MAIL_USERNAME"]
        MAIL_PASSWORD = env["MAIL_PASSWORD"]
        MAIL_DEFAULT_SENDER = env["MAIL_DEFAULT_SENDER"]

        # SQLALCHEMY CONFIG
        SQLALCHEMY_DATABASE_URI = "".join(
            [
                "postgresql+psycopg2://",
                str(env["DATABASE_USER"]),
                ":",
                str(env["DATABASE_PW"]),
                "@",
                str(env["DATABASE_HOST"]),
                ":",
                str(env["DATABASE_PORT"]),
                "/",
                str(env["DATABASE_NAME"]),
            ]
        )
    except Exception as e:
        print(e)
        raise e


class DevelopmentConfig(Config):

    from flask_talisman import DEFAULT_CSP_POLICY

    CSP = DEFAULT_CSP_POLICY
    try:
        env = dotenv_values(".env")

        # Flask-mail config
        MAIL_SERVER = env["MAIL_SERVER"]
        MAIL_PORT = int(env["MAIL_PORT"])
        MAIL_USE_TLS = env["MAIL_USE_TLS"] in ["True", "true", "TRUE"]
        MAIL_USE_SSL = env["MAIL_USE_SSL"] in ["True", "true", "TRUE"]
        MAIL_USERNAME = env["MAIL_USERNAME"]
        MAIL_PASSWORD = env["MAIL_PASSWORD"]
        MAIL_DEFAULT_SENDER = env["MAIL_DEFAULT_SENDER"]

    except Exception as e:
        print(e)
        raise e


class TestingConfig(Config):

    from flask_talisman import DEFAULT_CSP_POLICY

    CSP = DEFAULT_CSP_POLICY
    try:
        env = dotenv_values(".env")

        # Flask-mail config
        MAIL_SERVER = env["MAIL_SERVER"]
        MAIL_PORT = int(env["MAIL_PORT"])
        MAIL_USE_TLS = env["MAIL_USE_TLS"] in ["True", "true", "TRUE"]
        MAIL_USE_SSL = env["MAIL_USE_SSL"] in ["True", "true", "TRUE"]
        MAIL_USERNAME = env["MAIL_USERNAME"]
        MAIL_PASSWORD = env["MAIL_PASSWORD"]
        MAIL_DEFAULT_SENDER = env["MAIL_DEFAULT_SENDER"]
        TESTING = True

    except Exception as e:
        print(e)
        raise e
