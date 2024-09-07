from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
import os
import pathlib

path_templates = os.path.join(pathlib.Path(__file__).parent.resolve(), 
                              "templates")
dash = Blueprint("dash", __name__,  template_folder=path_templates)

@dash.route("/dashboard", methods = ["GET", "POST"])
@login_required
def dashboard():
    
    title = "Dashboard"
    page = "dashboard.html"
    return render_template("index.html", page=page, title=title)
    