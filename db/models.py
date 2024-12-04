class Usuario:
    def __init__(
        self,
        id_usuario=None,
        nombre=None,
        email=None,
        password=None,
        rol=None,
        fecha_registro=None,
    ):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.password = password
        self.rol = rol
        self.fecha_registro = fecha_registro

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "email": self.email,
            "password": self.password,
            "rol": self.rol,
            "fecha_registro": self.fecha_registro,
        }


class ParqueoEspacio:
    def __init__(
        self,
        id_espacio=None,
        ubicacion=None,
        estado=None,
    ):
        self.id_espacio = id_espacio
        self.ubicacion = ubicacion
        self.estado = estado

    def to_dict(self):
        return {
            "id_espacio": self.id_espacio,
            "ubicacion": self.ubicacion,
            "estado": self.estado,
        }


class Reserva:
    def __init__(
        self,
        id_reserva=None,
        id_usuario=None,
        id_espacio=None,
        fecha_reserva=None,
        hora_entrada=None,
        hora_salida=None,
    ):
        self.id_reserva = id_reserva
        self.id_usuario = id_usuario
        self.id_espacio = id_espacio
        self.fecha_reserva = fecha_reserva
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida

    def to_dict(self):
        return {
            "id_reserva": self.id_reserva,
            "id_usuario": self.id_usuario,
            "id_espacio": self.id_espacio,
            "fecha_reserva": self.fecha_reserva,
            "hora_entrada": self.hora_entrada,
            "hora_salida": self.hora_salida,
        }


class Vehiculo:
    def __init__(
        self,
        id_vehiculo=None,
        matricula=None,
        marca=None,
        modelo=None,
        color=None,
        id_usuario=None,
    ):
        self.id_vehiculo = id_vehiculo
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.id_usuario = id_usuario

    def to_dict(self):
        return {
            "id_vehiculo": self.id_vehiculo,
            "matricula": self.matricula,
            "marca": self.marca,
            "modelo": self.modelo,
            "color": self.color,
            "id_usuario": self.id_usuario,
        }
