from pydantic import BaseModel, Field, AnyUrl, EmailStr, field_validator, model_validator, computed_field
from typing import List, Dict, Annotated, Optional

class Address(BaseModel):

    city: str
    state: str
    pin: int

class Person(BaseModel):

    name: str
    weight: float
    email: EmailStr
    age: int
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    address: Address

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):

        valid_domain = ['hdfc.com', 'icici.com', 'axis.com']
        
        actual_value = value.split('@')[-1]

        if actual_value not in valid_domain:
            raise ValueError("Domain not available")
        return value
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, value):

        return value.upper()

    @model_validator(mode='after')
    def validate_model(self):

        if self.age > 50 and self.married is False:
            raise ValueError('Marry fast!!\nOr you will die VIRGIN!!')
        return self
    
    @computed_field
    @property
    def bmi(self) -> float:

        return round( self.weight/(self.height**2), 2 )

def person_details(person: Person):

    print('valid details, ')
    print(person.name)
    print(person.age)
    print(person.email)
    print(person.married)
    print(f"BMi: {person.bmi}")
    print(address1)
    print('done')


address_info = {'city' : 'solapur', 'state': 'Maharashtra', 'pin':'413003'}
address1 = Address(**address_info)

patient_info = {'name' : 'abc', 'age': 20, 'weight': 75, 'height': 1.72,'married': 0, 'email': 'abc@hdfc.com', 'linkedin_url': 'http://linkedin.com', 'allergies' : ['dust'],
            'contact_details': {'email' : 'vedantkolhapure111@gmail.com', 'number':'8788397356', 'emergency' : '123'}, 'address':address1}

person1 = Person(**patient_info)

person_details(person1)

temp = person1.model_dump_json()

print(temp)