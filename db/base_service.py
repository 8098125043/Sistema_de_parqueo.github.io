from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def add_item(self, item_data):
        pass

    @abstractmethod
    def get_all_items(self):
        pass

    @abstractmethod
    def get_item_by_id(self, item_id):
        pass

    @abstractmethod
    def get_item_by_custom_field(self, field_name, field_value):
        pass

    @abstractmethod
    def update_item(self, item_id, new_data):
        pass

    @abstractmethod
    def delete_item(self, item_id):
        pass