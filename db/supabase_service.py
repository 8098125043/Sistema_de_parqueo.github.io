from .base_service import BaseService
from supabase import create_client
from config import supabase_url, supabase_key

class SupabaseService(BaseService):
    def __init__(self, table_name):
        self.supabase_url = supabase_url
        self.supabase_key = supabase_key
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