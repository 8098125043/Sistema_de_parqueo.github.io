from flask import Blueprint, request, render_template, redirect, url_for
from routes.controllers import create_user, login_user
from db.services import ParqueoEspacioService, UsuarioService
from datetime import datetime

base = Blueprint("base", __name__)


@base.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@base.get("/inicio")
def inicio():
    return render_template("inicio.html")


@base.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            user = login_user(request.form)
            if user:
                return redirect(url_for("base.inicio"))
            else:
                return render_template(
                    "login.html", error="email o contraseña incorrectos"
                )
        except Exception as e:
            return render_template(
                "login.html", error="Error al iniciar sesión: " + str(e)
            )
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
    sevice = UsuarioService()
    users = sevice.get_all_usuarios()
    if users:
        return render_template("user.html", usuarios=users)
    return render_template("user.html", usuarios=None)


@base.route("/manage-parking", methods=["GET"])
def manage_parking():
    service = ParqueoEspacioService()
    parqueo_espacios = service.get_parqueo_espacios()
    if parqueo_espacios:
        return render_template("manage-parking.html", espacios=parqueo_espacios)
    return render_template("manage-parking.html", espacios=None)


@base.route("/entrada-vehiculo", methods=["GET", "POST"])
def entrada_vehiculo():
    sevice = ParqueoEspacioService()
    parqueo_espacios = sevice.get_parqueo_espacios()
    hora_actual = datetime.now()
    hora_actual = hora_actual.strftime("%H:%M")

    espacio_disponible = None
    for espacio in parqueo_espacios:
        if espacio.estado == "Disponible":
            espacio_disponible = espacio
            break

    if request.method == "POST":
        print(request.form.get("vehiclePlate"))
        print(request.form.get("driverName"))
        return render_template(
            "entrada-vehiculo.html", espacio=espacio, hora=hora_actual
        )

    if espacio_disponible:
        return render_template(
            "entrada-vehiculo.html", espacio=espacio_disponible, hora=hora_actual
        )

    return render_template("entrada-vehiculo.html", espacio=None, hora=hora_actual)


@base.get("/salida-vehiculo")
def salida_vehiculo():
    return render_template("salida_vehiculo.html")


@base.get("/contacto")
def contacto():
    return render_template("contact.html")
