from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint("auth", __name__)


@auth.route("/acceder")
def login():
    return render_template("login.html")


@auth.route("/registrarse")
def sign_up():
    return render_template("signup.html")


@auth.route("/cerrar-sesion")
def sign_out():
    return redirect(url_for("views.home"))

