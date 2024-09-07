from dotenv import load_dotenv
from uuid import uuid4
import platform
import os

from datetime import timedelta

load_dotenv()

login_db = os.getenv('login')
passwd_db = os.getenv('password')
host_db = os.getenv('host')
database_name = os.getenv('database')

## PARAMETROS PARA O APP FLASK
PDF_PATH = os.path.join(os.getcwd(), "PDF")
DOCS_PATH = os.path.join(os.getcwd(), "Docs")
TEMP_PATH = os.path.join(os.getcwd(), "Temp")
IMAGE_TEMP_PATH = os.path.join(TEMP_PATH, "IMG")
CSV_TEMP_PATH = os.path.join(TEMP_PATH, "csv")
PDF_TEMP_PATH = os.path.join(TEMP_PATH, "pdf")

debug = os.getenv('DEBUG', 'False').lower() in (
        'true', '1', 't', 'y', 'yes')

database_uri = f"mysql://{login_db}:{passwd_db}@{host_db}/{database_name}"
if debug is True:
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
    
    if not os.path.exists(paths):
        os.makedirs(paths, exist_ok=True)
        
    else:
        
        plataforma = platform.system()
        
        if plataforma == "Linux":
            path =  f"{paths}/*" 
            comand = "rm -r " + path
             
        
        elif plataforma == "Windows":
            path =  f"{paths}\\*" 
            command = "powershell rm -r " + path
        
        os.system(command)


