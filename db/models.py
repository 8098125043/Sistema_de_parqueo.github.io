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
