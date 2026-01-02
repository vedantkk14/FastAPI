from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(default=..., description='ID of the patients', examples=['P001'])]
    name: Annotated[str, Field(default=..., description='Name of patient: ', max_length=50)]
    city: Annotated[str, Field(default=..., description='City where the patient lives: ')]
    age: Annotated[int, Field(default=..., gt=0, lt=90, description='Age of the patient: ')]
    gender: Annotated[Literal['male', 'Male', 'MALE','female', 'Female', 'FEMALE', 'other'], Field(default=..., description='Gender of patient: ') ]
    height: Annotated[float, Field(default=..., gt=0, description='Height of the patient: ')]
    weight: Annotated[float, Field(default=..., gt=0, description='Enter weight of the patient in kgs: ')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        else:
            return 'Obese' 

def load_data():

    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):

    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.get('/')
def home():
    return {'message' : 'Home page.'}

@app.get('/view')
def view_data():

    data = load_data()
    return data

@app.post('/create')
def create_patient(patient: Patient):
    
    #load data
    data = load_data()

    #check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')
    
    #new patients added to database
    data[patient.id] = patient.model_dump(exclude='id')

    #save to json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message' : 'Patient created successfully!'})

