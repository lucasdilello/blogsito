from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/acceder")
def login():
    return "Acceder"

@auth.route("/registrarse")
def sign_up():
    return "Registrarse"

@auth.route("/cerrar-sesion")
def sign_out():
    return "Salir"

