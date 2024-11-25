import os
import shutil
from datetime import timedelta
from pathlib import Path
from uuid import uuid4

from dotenv import dotenv_values

values = dotenv_values(os.path.join(os.getcwd(), ".env"))

login_db = values.get("login")
passwd_db = values.get("password")
host_db = values.get("host")
database_name = values.get("database")

# PARAMETROS PARA O APP FLASK
PDF_PATH = os.path.join(os.getcwd(), "PDF")
DOCS_PATH = os.path.join(os.getcwd(), "Docs")
TEMP_PATH = os.path.join(os.getcwd(), "Temp")
IMAGE_TEMP_PATH = os.path.join(TEMP_PATH, "IMG")
CSV_TEMP_PATH = os.path.join(TEMP_PATH, "csv")
PDF_TEMP_PATH = os.path.join(TEMP_PATH, "pdf")
DEBUG = True

# database_uri = f"mysql://{login_db}:{passwd_db}@{host_db}/{database_name}"
# if debug is True:
#     database_uri = "sqlite:///project.db"

database_uri = "sqlite:///project.db"
SQLALCHEMY_DATABASE_URI = database_uri

SQLALCHEMY_TRACK_MODIFICATIONS = False
PREFERRED_URL_SCHEME = "https"
SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = True
PERMANENT_SESSION_LIFETIME = timedelta(days=31).max.seconds
SRC_IMG_PATH = os.path.join(os.getcwd(), "app", "src", "assets", "img")
SECRET_KEY = str(uuid4())

for paths in [DOCS_PATH, TEMP_PATH, IMAGE_TEMP_PATH, CSV_TEMP_PATH, PDF_TEMP_PATH]:

    path_folder = Path(paths)

    if path_folder.exists():
        shutil.rmtree(str(path_folder))

    path_folder.mkdir(exist_ok=True)
