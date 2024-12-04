from flask import Blueprint, request, render_template, redirect, url_for
from routes.controllers import create_user

base = Blueprint("base", __name__)


@base.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@base.get("/inicio")
def inicio():
    return render_template("inicio.html")


@base.get("/login")
def login():
    return render_template("login.html")


@base.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        try:
            user = create_user(request.form)
            if user:
                return redirect(url_for("base.login"))
            else:
                return render_template(
                    "registro.html", error="El correo ya está registrado"
                )
        except Exception as e:
            return render_template(
                "registro.html", error="Error al crear el usuario: " + str(e)
            )

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


@base.get("/salida-vehiculo")
def salida_vehiculo():
    return render_template("salida-vehiculo.html")


@base.get("/contacto")
def contacto():
    return render_template("contact.html")
