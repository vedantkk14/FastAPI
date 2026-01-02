from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(default=None, max_length=50, title='Name of the student: ', examples=['vedant', 'vrishabh'])]
    age: int = Field(gt=10, le=80)
    weight: Annotated[ float, Field(gt=0, lt=120, strict=True) ]
    email: EmailStr
    linkedin_url: Annotated[AnyUrl, Field(default='http://linkedin.com')]
    married: Annotated[ Optional[bool], Field(default=False, description='Enter your maritual status: ', examples=['True', 'False']) ]
    allergies: Optional[List[str]] = Field(max_length=5, default=None)
    contact_details: Dict[str, str]

def patient_details(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.married)
    print('done')

patient_info = {'name' : 'abc', 'age': 20, 'weight': 75, 'married': 0, 'email': 'abc@gmail.com', 'linkedin_url': 'http://linkedin.com',
            'contact_details': {'email' : 'vedantkolhapure111@gmail.com', 'number':'8788397356'}}

patient1 = Patient(**patient_info)

patient_details(patient1)