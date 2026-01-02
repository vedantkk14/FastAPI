# At this point:
#     All fields are validated
#     The object already exists
#     self is available

# So:
#     Validation is instance-based
#     You inspect multiple fields together

# No @classmethod is needed.


from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    weight: float
    email: EmailStr
    age: int
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    ## model validator- can combine multiple fields and validate all together
    # here, if the person is above age 60, they should have emergency contact in their contact details
    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if self.age > 60 and "emergency" not in self.contact_details:
            raise ValueError(
                "Patients older than 60 must have an emergency contact"
            )
        return self

def patient_details(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.married)
    print('done')

patient_info = {'name' : 'abc', 'age': 70, 'weight': 75, 'married': 0, 'email': 'abc@hdfc.com', 'linkedin_url': 'http://linkedin.com', 'allergies' : ['dust'],
            'contact_details': {'email' : 'vedantkolhapure111@gmail.com', 'number':'8788397356', 'emergency' : '123'}}

patient1 = Patient(**patient_info)

patient_details(patient1)