from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SqliteService(BaseService):
    def __init__(self, table_name, db_path = "database.db"):
        self.engine = create_engine(f'sqlite:///{db_path}')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.table_name = table_name
        
        # Verifica si la tabla existe
        if not self.table_exists():
            raise ValueError(f"La tabla '{table_name}' no existe en la base de datos")

    def table_exists(self):
        return self.engine.has_table(self.table_name)

    def add_item(self, item_data):
        item = self.model(data=item_data)
        self.session.add(item)
        self.session.commit()
        return item.id

    def get_all_items(self):
        return self.session.query(self.model).all()

    def get_item_by_id(self, item_id):
        return self.session.query(self.model).get(item_id)

    def get_item_by_custom_field(self, field_name, field_value):
        return self.session.query(self.model).filter(getattr(self.model, field_name) == field_value).first()

    def update_item(self, item_id, new_data):
        item = self.get_item_by_id(item_id)
        if item:
            item.data = new_data
            self.session.commit()
            return item
        return None

    def delete_item(self, item_id):
        item = self.get_item_by_id(item_id)
        if item:
            self.session.delete(item)
            self.session.commit()
            return True
        return False