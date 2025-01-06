from pydantic import BaseModel, ValidationError
'''
class User(BaseModel):
    name: str
    age: int
    email: str

try:
    user = User(name="John Doe", age="25", email="john@example.com")
    print(user)
except ValidationError as e:
    print(e)
'''

#############################################

# Product
'''
class Product(BaseModel):
    name: str
    price: float
    quantity: int

valid_data = {
    'name' : 'Chips',
    'price' : 20.5,
    'quantity' : 1
}


try : 
    product = Product(**valid_data)
    print(product)
except ValidationError as e:
    print(e)


invalid_data = {
    'name' : 'Chips',
    'price' : 'twenty',
    'quantity' : 'one'
}


try : 
    product = Product(**invalid_data)
    print(product)
except ValidationError as e:
    print(e)
'''



#################################################################################




# Street name
'''
class Street(BaseModel):
    name : str
    city : str
    zipcode : str

valid_data = {
    'name' : 'Singhpura',
    'city' : 'Zirakpur',
    'zipcode' : '140603'
}

try :
    street = Street(**valid_data)
    print(street)
except ValidationError as e:
    print(e)


invalid_data = {
    'name' : 'Singhpura',
    'city' : 'Zirakpur',
    'zipcode' : '140-603'
}

try :
    street = Street(**invalid_data)
    print(street)
except ValidationError as e:
    print(e)
'''




#################################################################################


'''
class Address(BaseModel) :
    street : str
    city : str
    zipcode : int

class Person(BaseModel) :
    name : str
    age : int
    address : Address

valid_data = {
    'name' : 'Alice',
    'age' : '21',
    'address' : {
        'street' : '72 Xavier',
        'city' : 'LA',
        'zipcode' : '1098'
    }
}

try :
    person = Person(**valid_data)
    print(person)
except ValidationError as e:
    print(e)


invalid_data = {
    'name' : 'Alice',
    'age' : '21',
}

try :
    person = Person(**invalid_data)
    print(person)
except ValidationError as e:
    print(e)
'''




#################################################################################




from typing import Optional
'''
class Event(BaseModel):
    event_name: str
    event_date : Optional[str] = None
    is_virtual : bool = False

valid_data = {
    'event_name' : 'Holi Festival',
    'event-date' : '20-01-2025',
    'is_virtual' : False
}

try :
    event = Event(**valid_data)
    print(event)
except ValidationError as e:
    print(e)


valid_data_without_date = {
    'event_name' : 'Holi Festival',
    'is_virtual' : False
}

try :
    event = Event(**valid_data)
    print(event)
except ValidationError as e:        # This will not throw an error because we gave optional in date
    print(e)
'''




###########################################################

class Person(BaseModel):
    name : str
    age : int

class Employee(Person):
    job_title : str

class Manager(Person):
    department: str


employee_data = {
    'name' : 'Nazim',
    'age' : 20,
    'job_title' : 'Data Engineer',
}

try :
    employee = Employee(**employee_data)
    print(employee)
except ValidationError as e:
    print(e)


manager_data = {
    'name' : 'Nazim',
    'age' : 21,
    'department' : 'Engineering'
}

try :
    manager = Manager(**manager_data)
    print(manager)
except ValidationError as e:
    print(e)
