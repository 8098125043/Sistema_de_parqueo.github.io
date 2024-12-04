from config import supabase_key, supabase_url
from supabase import create_client
from db.models import Usuario
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
