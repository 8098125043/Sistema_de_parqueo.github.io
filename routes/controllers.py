from flask import Blueprint, jsonify, request
from datetime import datetime
from db.services import (
    UsuarioService,
    ParqueoEspacioService,
    VehiculoService,
    ReservaService,
)

controllers = Blueprint("controllers", __name__, url_prefix="/api/")


@controllers.route("/users_test", methods=["GET"])
def get_users_test():
    try:
        service = UsuarioService()
        # print(service.get_all_usuarios()[0].to_dict())
        user = service.get_usuario_by_id(6)
        print(user)

        if user:
            return jsonify({"status": "success", "user": user.to_dict()}), 201
        return jsonify({"error": "Error al crear el usuario"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@controllers.route("/users", methods=["GET"])
def get_users():
    service = UsuarioService()
    users = service.get_all_usuarios()
    return jsonify(users)


@controllers.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    service = UsuarioService()
    user = service.get_usuario_by_id(id)
    return jsonify(user)


@controllers.route("/users", methods=["POST"])
def create_user_route():
    try:
        user = create_user(request.json())
        if user:
            return jsonify({"status": "success", "user": user.to_dict()}), 201
        return jsonify({"error": "Error al crear el usuario"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# utilidades
def create_user(data=None):
    if data:
        nombre = data.get("nombre")
        email = data.get("email")
        password = data.get("password")
        rol = data.get("tipoEmpleado")
    else:
        nombre = request.json.get("nombre")
        email = request.json.get("email")
        password = request.json.get("password")
        rol = request.json.get("tipoEmpleado")

    service = UsuarioService()
    return service.create_usuario(
        nombre=nombre,
        email=email,
        password=password,
        rol=rol,
    )


def entrada_vehiculo(data=None):
    if data:
        matricula = data.get("vehiclePlate")
        nombre_conductor = data.get("driverName")
        hora_entrada = data.get("entryTime")
        ubicacion = data.get("parkingSpace")
    else:
        matricula = request.json.get("vehiclePlate")
        nombre_conductor = request.json.get("driverName")
        hora_entrada = request.json.get("entryTime")
        ubicacion = request.json.get("parkingSpace")

    espacio_service = ParqueoEspacioService()
    espacio = espacio_service.get_parqueo_espacios_by_ubicacion(ubicacion)

    if espacio:
        service = VehiculoService()
        vehiculo = service.get_vehiculo_by_matricula(matricula)
        if not vehiculo:
            vehiculo = service.create_vehiculo(
                matricula, None, None, None, 2,
            )

        if vehiculo:
            reserva_service = ReservaService()
            reserva_service.create_reserva(
                None,
                espacio.id_espacio,
                vehiculo.id_vehiculo,
                datetime.now().strftime("%Y-%m-%d"),
                hora_entrada,
                None,
            )
            espacio_service.update_parqueo_espacio(espacio.id_espacio, None, "ocupado")
            return vehiculo
    return None


def login_user(data=None):
    if data:
        email = data.get("email")
        password = data.get("password")
    else:
        email = request.json.get("email")
        password = request.json.get("password")

    service = UsuarioService()
    user = service.get_usuario_by_email(email)

    if user and user.password == password:
        return user
    return None
