def authorize_order(client: (str, int), items: [(str, int)]): -> dict:
    # Абстрактное решение тут
	  person: Person = get_person(*client)
    checked_items = {i: person.can_buy(get_item(i)) for i in items}
    return checked_items
    

def get_person_from_db(person_type, person_id) :
    ...    
                
def get_item_from_db(item_type, item_id) :
    ...
    
def get_recipt_from_db(person_id, item_id):
	  ...

    
def get_person(name, id):
	if name == 'doctor':
  	return Doctor(name, id, get_person_from_db(name, id).speciality_id)
  if name == 'client':
  	return Client(name, id)

class Person:
	def __init__(id):
    self.id = id
  
class Client(Person):
	def __init__(id: int):
  	super().__init__(id)
    
	def is_reciept_exist(item_id):
  	return get_recipt_from_db(self.id, item_id) is not None

  def can_buy(item: Item) -> bool:
  	if isinstance(item) == CommonItem:
    	return true
    if isinstance(item) == SpecialItem:
    	return false
    if isinstance(item) == RecieptItem:
    	return is_reciept_exist(item.id)
  	  
class Doctor(Person):
	def __init__(id: int, speciality_id: int):
  	super().__init__(id)
		self.speciality_id = speciality_id
    
  def is_spicially_allowed(item):
		return self.speciality_id == item.speciality_id
    
  def can_buy(item: Item) -> bool:
  	if isinstance(item) == CommonItem or isinstance(item) == RecieptItem:
    	return true
    if isinstance(item) == SpecialItem:
    	return is_spicially_allowed()


def get_item(name, id):
	if name == 'common_items':
  	return CommonItem(id)
	if name == 'special_items':
  	return SpecialItem(id, get_item_from_db(item.name, item.id).speciality_id)

class Item:
	def __init__(id: int):
    self.id = id
    
class CommonItem(Item):
	def __init__(id: int):
  	super().__init__(id)
	
class RecieptItem(Item):
	def __init__(id: int):
  	super().__init__(id)
    
class SpecialItem(Item):
	def __init__(id: int, speciality_id: int):
  	super().__init__(id)
    self.speciality_id = speciality_id
  

  






