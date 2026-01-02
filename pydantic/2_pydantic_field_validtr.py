# Field validators are class-level hooks applied to a field definition, so Pydantic calls them as class methods, 
# while model validators (after mode) operate on an already-created instance and therefore use instance methods.

# field_validator->validates single field-> it runs during field parsing->it receives field value
# The model instance does not exist yet,
# Pydantic is still
    # parsing raw input
    # validating types
    # building fields one by one
# That’s why @classmethod is required in field_validator.


from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    weight: float
    email: EmailStr
    age: int
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    ## field validator works on a single field
    # field validator- here used to validate email such that the client should only have valid_domains in their email, eg abc@hdfc.com.
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    #field validator- here used to validate name, the name should be always capital
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):

        return value.upper()
    

    #Type coercion is the automatic conversion of a value from one data type 
    #here the value before type coersion is checked, by default(the mode='after', i.e. type coersion occurs)
    #but here we check the value before tpye coersion
    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be between 0 and 100')

def patient_details(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.married)
    print('done')

patient_info = {'name' : 'abc', 'age': 20, 'weight': 75, 'married': 0, 'email': 'abc@hdfc.com', 'linkedin_url': 'http://linkedin.com', 'allergies' : ['dust'],
            'contact_details': {'email' : 'vedantkolhapure111@gmail.com', 'number':'8788397356', 'emergency' : '123'}}

patient1 = Patient(**patient_info)

patient_details(patient1)