from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated, Optional, Literal
import json

app = FastAPI()

class Patient(BaseModel):
    id:Annotated[str, Field(..., description="The ID of the patient",examples=["p001"])]
    name:Annotated[str, Field(..., description="The name of the patient",examples=["sathvik"])]
    city:Annotated[str, Field(..., description="The city of the patient",examples=["bangalore"])]
    age:Annotated[int,Field(..., description="The age of the patient",gt=0,lt=120,examples=[20])]
    gender:Annotated[Literal["male","female","others"], Field(..., description="The gender of the patient",examples=["male"])]
    height:Annotated[float, Field(..., description="The height of the patient in meters",examples=[1.75],gt=0)]
    weight:Annotated[float, Field(..., description="The weight of the patient in kilograms",examples=[70.0],gt=0)]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi= round(self.weight / (self.height ** 2),2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi<18.5:
            return "Underweight"
        elif 18.5<=self.bmi<25:
            return "Normal weight"
        elif 25<=self.bmi<30:
            return "Overweight"
        else:
            return "Obese"




def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

def save_data(data):
    with open("patients.json", "w") as file:
        json.dump(data, file)


@app.get("/")
def hello():
    return {"message": "PATIENT MANAGEMENT SYSTEM API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records, built with FastAPI and Pydantic."}



@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    # Include the patient ID in the results
    patients_with_ids = [{"id": patient_id, **patient_data} for patient_id, patient_data in data.items()]
    sorted_data = sorted(patients_with_ids, key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()#load the existing data from the file
    if patient.id in data:#check if the patient with the same ID already exists
        raise HTTPException(status_code=400, detail="Patient with this ID already exists.")
    
   
    data[patient.id] = patient.model_dump(exclude=["id"])#exclude the id field from the patient data and add the patient data to the existing data using the patient ID as the key
    
    save_data(data)#save the updated data back to the json file

    return JSONResponse(content={"message": "Patient created successfully"}, status_code=201)