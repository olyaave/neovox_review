from abc import ABC, abstractmethod
from enum import Enum


def authorize_order(client: (str, int), items: [(str, int)]) -> dict:
    # Абстрактное решение тут
    person: Person = get_person(*client)
    checked_items = {i: person.can_buy(get_item(i)) for i in items}
    return checked_items


def get_person_from_db(person_type: str, person_id: int):
    ...


def get_item_from_db(item_type: str, item_id: int):
    ...


def get_recipe_from_db(person_id: int, item_id: int):
    ...


class PersonTypeEnum(Enum, str):
    doctor = "doctor"
    client = "client"


class ItemTypeEnum(Enum, str):
    special_item = "special_item"
    receipt_item = "receipt_item"
    common_item = "common_item"


def is_recipe_exist(person_id: int, item_id: int) -> bool:
    return get_recipe_from_db(person_id, item_id) is not None


def is_specially_allowed(person, item):
    return get_person_from_db(*person).speciality_id == item.speciality_id


class Permission(ABC):

    @abstractmethod
    def can_buy(self, person_id, item) -> bool:
        pass


class ClientPermission(Permission):
    def can_buy(self, person_id, item) -> bool:
        if isinstance(item, CommonItem):
            return True
        if isinstance(item, SpecialItem):
            return False
        if isinstance(item, RecipeItem):
            return is_recipe_exist(person_id, item.id)


class DoctorPermission(Permission):
    def can_buy(self, person_id, item) -> bool:
        if isinstance(item, (CommonItem, RecipeItem)):
            return True
        if isinstance(item, SpecialItem):
            return is_specially_allowed((PersonTypeEnum.doctor, person_id), item)


def get_person(person_type: str, person_id: int):
    persons = {PersonTypeEnum.doctor: Doctor,
               PersonTypeEnum.client: Client}
    return persons[PersonTypeEnum(person_type)](person_id)


def get_item(item_name, item_id):
    items = {ItemTypeEnum.common_item: CommonItem,
             ItemTypeEnum.special_item: SpecialItem,
             ItemTypeEnum.receipt_item: RecipeItem}
    return items[ItemTypeEnum(item_name)](item_id)


class Item:
    def __init__(self, id: int):
        self.id = id


class CommonItem(Item):
    def __init__(self, id: int):
        super().__init__(id)


class RecipeItem(Item):
    def __init__(self, id: int):
        super().__init__(id)


class SpecialItem(Item):
    def __init__(self, id: int, speciality_id: int):
        super().__init__(id)
        self.speciality_id = speciality_id


class Person(ABC):
    def __init__(self, person_id: int):
        self.person_id: int = person_id
        self.permissions = Permission()

    def can_buy(self, item: Item) -> bool:
        return self.permissions.can_buy(self.person_id, item)


class Client(Person):
    def __init__(self, person_id: int):
        super().__init__(person_id)
        self.permissions = ClientPermission()


class Doctor(Person):
    def __init__(self, person_id: int):
        super().__init__(person_id)
        self.permissions = DoctorPermission()

















