from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    
    return data

@app.get('/')
def hello():
    return {'message' :'Patient Management System API'}

@app.get('/about')
def about():
    return {'message' : 'A fully functional API to manage your patient records.'} 

@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/patient/{patient_id}')                # a path parameter- They are the variable parts of the URL.
def view_patient(patient_id: str = Path(default=..., description='ID of the patient in DB', example='P001')):
    # load all patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')       # custom exception

@app.get('/sort')
def sort_patients(sort_by: str = Query(default=..., description='Sort on the basis of height, weight or BMI'), order: str = Query(default='asc', description='Sort in ascending or descending order')):
    
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid fields, select from {valid_fields}')   #bad req error
    
    valid_order = ['asc', 'desc']
    if order not in valid_order:
        raise HTTPException(status_code=400, detail=f'Invalid order, select from {valid_order}')
    
    data = load_data()
    
    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data