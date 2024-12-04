from config import supabase_key, supabase_url
from supabase import create_client
from db.models import Usuario, ParqueoEspacio, Vehiculo, Reserva
from datetime import datetime


class BaseService:
    def add_item(self, item_data):
        pass

    def get_all_items(self):
        pass

    def get_item_by_id(self, item_id):
        pass

    def update_item(self, item_id, new_data):
        pass

    def delete_item(self, item_id):
        pass


class SupabaseService(BaseService):
    def __init__(self, table_name):
        self.supabase_url = supabase_url
        self.supabase_key = supabase_key
        # self.supabase_secret = os.environ.get('SUPABASE_SECRET')
        self.supabase = create_client(self.supabase_url, self.supabase_key)
        self.table_name = table_name

    def add_item(self, item_data):
        result = self.supabase.from_(self.table_name).insert([item_data]).execute()
        return result.data

    def get_all_items(self):
        result = self.supabase.from_(self.table_name).select("*").execute()
        return result.data

    def get_item_by_id(self, item_id, id_field="id"):
        result = (
            self.supabase.from_(self.table_name)
            .select("*")
            .eq(id_field, item_id)
            .execute()
        )
        return result.data[0] if result.data else None

    def get_item_by_custom_field(self, field_name, field_value):
        result = (
            self.supabase.from_(self.table_name)
            .select("*")
            .eq(field_name, field_value)
            .execute()
        )
        return result.data[0] if result.data else None

    def update_item(self, item_id, new_data):
        result = (
            self.supabase.from_(self.table_name)
            .update({"id": item_id})
            .set(new_data)
            .execute()
        )
        return result.data[0]

    def delete_item(self, item_id):
        result = self.supabase.from_(self.table_name).delete({"id": item_id}).execute()
        if result.error:
            print(result.error)
        return result


class UsuarioService:
    def __init__(self, supabase_service: SupabaseService = None):
        if supabase_service is None:
            supabase_service = SupabaseService("usuarios")
        self.supabase_service = supabase_service

    def get_all_usuarios(self):
        result = self.supabase_service.get_all_items()
        usuarios = []
        for row in result:
            usuario = Usuario(
                id_usuario=row["id_usuario"],
                nombre=row["nombre"],
                email=row["email"],
                password=row["password"],
                rol=row["rol"],
                fecha_registro=row["fecha_registro"],
            )
            usuarios.append(usuario)
        return usuarios

    def get_usuario_by_id(self, id_usuario):
        result = self.supabase_service.get_item_by_id(id_usuario, "id_usuario")
        if result:
            return Usuario(
                id_usuario=result["id_usuario"],
                nombre=result["nombre"],
                email=result["email"],
                password=result["password"],
                rol=result["rol"],
                fecha_registro=result["fecha_registro"],
            )
        return None

    def get_usuario_by_email(self, email):
        result = self.supabase_service.get_item_by_custom_field("email", email)
        if result:
            return Usuario(
                id_usuario=result["id_usuario"],
                nombre=result["nombre"],
                email=result["email"],
                password=result["password"],
                rol=result["rol"],
                fecha_registro=result["fecha_registro"],
            )
        return None

    def create_usuario(self, nombre, email, password, rol):
        fecha_registro = datetime.now()
        fecha_registro = fecha_registro.strftime("%d-%m-%Y")
        data = {
            "nombre": nombre,
            "email": email,
            "password": password,
            "rol": rol,
            "fecha_registro": fecha_registro,
        }
        result = self.supabase_service.add_item(data)
        if result:
            return Usuario(
                id_usuario=result[0]["id_usuario"],
                nombre=nombre,
                email=email,
                rol=rol,
                fecha_registro=fecha_registro,
            )
        return None

    def update_usuario(self, id_usuario, nombre, email, password, rol):
        data = {"nombre": nombre, "email": email, "password": password, "rol": rol}
        result = self.supabase_service.update_item(id_usuario, data)
        if result:
            return Usuario(
                id_usuario=id_usuario,
                nombre=nombre,
                email=email,
                rol=rol,
                fecha_registro=self.get_usuario_by_id(id_usuario).fecha_registro,
            )
        return None

    def delete_usuario(self, id_usuario):
        return self.supabase_service.delete_item(id_usuario)


class ParqueoEspacioService(SupabaseService):
    def __init__(self):
        super().__init__("parqueo_espacios")

    def get_parqueo_espacios_by_ubicacion(self, ubicacion):
        result = self.get_item_by_custom_field("ubicacion", ubicacion)
        if result:
            return ParqueoEspacio(
                id_espacio=result["id_espacio"],
                ubicacion=result["ubicacion"],
                estado=result["estado"],
            )
        return None

    def get_parqueo_espacio(self, id_espacio):
        result = self.get_item_by_id(id_espacio)
        if result:
            return ParqueoEspacio(
                id_espacio=result["id_espacio"],
                ubicacion=result["ubicacion"],
                estado=result["estado"],
            )
        return None

    def get_parqueo_espacios(self):
        result = self.get_all_items()
        parqueo_espacios = []
        for row in result:
            parqueo_espacio = ParqueoEspacio(
                id_espacio=row["id_espacio"],
                ubicacion=row["ubicacion"],
                estado=row["estado"],
            )
            parqueo_espacios.append(parqueo_espacio)
        return parqueo_espacios

    def create_parqueo_espacio(self, ubicacion, estado="Disponible"):
        data = {"ubicacion": ubicacion, "estado": estado}
        result = self.add_item(data)

        if result:
            return ParqueoEspacio(
                id_espacio=result[0]["id_espacio"],
                ubicacion=ubicacion,
                estado=estado,
            )
        return None

    def update_parqueo_espacio(self, id_espacio, parqueo_espacio=None, estado=None):
        parqueo_espacio_exist = self.get_parqueo_espacio(id_espacio)

        if parqueo_espacio_exist is None:
            return None

        parqueo_espacio_exist.ubicacion = (
            parqueo_espacio or parqueo_espacio_exist.ubicacion
        )
        parqueo_espacio_exist.estado = estado or parqueo_espacio_exist.estado

        data = {
            "ubicacion": parqueo_espacio_exist.ubicacion,
            "estado": parqueo_espacio_exist.estado,
        }
        result = self.update_item(id_espacio, data)
        if result:
            return parqueo_espacio_exist
        return None

    def delete_parqueo_espacio(self, id_espacio):
        return self.delete_item(id_espacio)


class VehiculoService(SupabaseService):
    def __init__(self):
        super().__init__("vehiculos")

    def get_vehiculo_by_matricula(self, matricula):
        result = self.get_item_by_custom_field("matricula", matricula)
        if result:
            return Vehiculo(
                id_vehiculo=result["id_vehiculo"],
                matricula=result["matricula"],
                marca=result["marca"],
                modelo=result["modelo"],
                color=result["color"],
                id_usuario=result["id_usuario"],
            )
        return None

    def get_vehiculo(self, id_vehiculo):
        result = self.get_item_by_id(id_vehiculo)
        if result:
            return Vehiculo(
                id_vehiculo=result["id_vehiculo"],
                matricula=result["matricula"],
                marca=result["marca"],
                modelo=result["modelo"],
                color=result["color"],
                id_usuario=result["id_usuario"],
            )
        return None

    def create_vehiculo(self, matricula, marca, modelo, color, id_usuario):
        data = {
            "matricula": matricula,
            "marca": marca,
            "modelo": modelo,
            "color": color,
            "id_usuario": id_usuario,
        }
        result = self.add_item(data)
        if result:
            return Vehiculo(
                id_vehiculo=result[0]["id_vehiculo"],
                matricula=matricula,
                marca=marca,
                modelo=modelo,
                color=color,
                id_usuario=id_usuario,
            )
        return None

    def update_vehiculo(self, id_vehiculo, matricula, marca, modelo, color):
        vehiculo_exist = self.get_vehiculo(id_vehiculo)

        if vehiculo_exist is None:
            return None

        data = {
            "matricula": matricula or vehiculo_exist.matricula,
            "marca": marca or vehiculo_exist.marca,
            "modelo": modelo or vehiculo_exist.modelo,
            "color": color or vehiculo_exist.color,
        }
        result = self.update_item(id_vehiculo, data)
        if result:
            return Vehiculo(
                id_vehiculo=id_vehiculo,
                matricula=matricula,
                marca=marca,
                modelo=modelo,
                color=color,
                id_usuario=vehiculo_exist.id_usuario,
            )
        return None

    def delete_vehiculo(self, id_vehiculo):
        return self.delete_item(id_vehiculo)

    def get_vehiculos(self):
        result = self.get_all_items()
        vehiculos = []
        for row in result:
            vehiculos.append(
                Vehiculo(
                    id_vehiculo=row["id_vehiculo"],
                    matricula=row["matricula"],
                    marca=row["marca"],
                    modelo=row["modelo"],
                    color=row["color"],
                    id_usuario=row["id_usuario"],
                )
            )
        return vehiculos


class ReservaService(SupabaseService):
    def __init__(self):
        super().__init__("reservas")

    def get_reserva(self, id_reserva):
        result = self.get_item_by_id(id_reserva)
        if result:
            return Reserva(
                id_reserva=result["id_reserva"],
                id_usuario=result["id_usuario"],
                id_espacio=result["id_espacio"],
                fecha_reserva=result["fecha_reserva"],
                hora_entrada=result["hora_entrada"],
                hora_salida=result["hora_salida"],
            )
        return None

    def create_reserva(
        self,
        id_reserva,
        id_espacio=None,
        fecha_reserva=None,
        hora_entrada=None,
        hora_salida=None,
    ):
        data = {
            "id_usuario": 27,
            "id_espacio": id_espacio,
            "fecha_reserva": fecha_reserva,
            "hora_entrada": hora_entrada,
            "hora_salida": hora_salida,
        }
        result = self.add_item(data)
        if result:
            return Reserva(
                id_reserva=id_reserva,
                id_usuario=27,
                id_espacio=id_espacio,
                fecha_reserva=fecha_reserva,
                hora_entrada=hora_entrada,
                hora_salida=hora_salida,
            )
        return None

    def update_reserva(
        self,
        id_reserva,
        id_espacio=None,
        fecha_reserva=None,
        hora_entrada=None,
        hora_salida=None,
    ):
        reserva_exist = self.get_reserva(id_reserva)

        if reserva_exist is None:
            return None

        data = {
            "id_usuario": reserva_exist.id_usuario,
            "id_espacio": id_espacio or reserva_exist.id_espacio,
            "fecha_reserva": fecha_reserva or reserva_exist.fecha_reserva,
            "hora_entrada": hora_entrada or reserva_exist.hora_entrada,
            "hora_salida": hora_salida or reserva_exist.hora_salida,
        }
        result = self.update_item(id_reserva, data)
        if result:
            return Reserva(
                id_reserva=id_reserva,
                id_usuario=data["id_usuario"],
                id_espacio=data["id_espacio"],
                fecha_reserva=data["fecha_reserva"],
                hora_entrada=data["hora_entrada"],
                hora_salida=data["hora_salida"],
            )
        return None

    def delete_reserva(self, id_reserva):
        return self.delete_item(id_reserva)

    def get_reservas(self):
        result = self.get_all_items()
        reservas = []
        for row in result:
            reserva = Reserva(
                id_reserva=row["id_reserva"],
                id_usuario=row["id_usuario"],
                id_espacio=row["id_espacio"],
                fecha_reserva=row["fecha_reserva"],
                hora_entrada=row["hora_entrada"],
                hora_salida=row["hora_salida"],
            )
            reservas.append(reserva)
        return reservas
