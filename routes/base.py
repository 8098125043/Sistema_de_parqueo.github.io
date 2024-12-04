from flask import Blueprint, render_template  # request, jsonify

base = Blueprint("base", __name__)


@base.get("/")
def index():
    return render_template("index.html")


@base.get("/inicio")
def inicio():
    return render_template("inicio.html")


@base.get("/login")
def login():
    return render_template("login.html")


@base.get("/registro")
def registro():
    return render_template("registro.html")


@base.get("/user")
def user():
    return render_template("user.html")


@base.get("/manage-parking")
def manage_parking():
    return render_template("manage-parking.html")


@base.get("/entrada-vehiculo")
def entrada_vehiculo():
    return render_template("entrada-vehiculo.html")


@base.get("contacto")
def contacto():
    return render_template("contact.html")
