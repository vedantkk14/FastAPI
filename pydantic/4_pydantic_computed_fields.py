from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    weight: float
    email: EmailStr
    age: int
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi


def patient_details(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.bmi)
    print('done')

patient_info = {'name' : 'abc', 'age': 70, 'weight': 75, 'height': 1.72,'married': 0, 'email': 'abc@hdfc.com', 'linkedin_url': 'http://linkedin.com', 'allergies' : ['dust'],
            'contact_details': {'email' : 'vedantkolhapure111@gmail.com', 'number':'8788397356', 'emergency' : '123'}}

patient1 = Patient(**patient_info)

patient_details(patient1)