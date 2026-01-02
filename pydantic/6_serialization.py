from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city' : 'solapur', 'state':'maharashtra', 'pin':'413003'}
address1 = Address(**address_dict)

patient_dict = {'name':'vedant', 'age':35, 'address':address1}
patient1 = Patient(**patient_dict)

# temp = patient1.model_dump()
temp = patient1.model_dump(exclude_unset=True)
# temp = patient1.model_dump_json()

print(temp)
print(type(temp))