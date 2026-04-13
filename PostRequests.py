from fastapi import FastAPI, Path, HTTPException, Query
from dataLoader import loadData, saveData
from pydantic import BaseModel, Field, computed_field
import json
from typing import Annotated, Literal
from fastapi.responses import JSONResponse


app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID of the patient", examples= ["P001"])]
    name: Annotated[str, Field(..., description="Name of the ID", examples=["Jonny"])]
    City: Annotated[str, Field(description="Living city of patient.", examples=["Kathmandu"])]
    age: Annotated[int, Field(..., gt=0, lt= 120,description="Current age of Patient.", examples=[20])]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of Patient', examples=['male'])]
    height: Annotated[float, Field(..., gt=0, description="Height of patient in mtrs.", examples=[10.5])]
    weight: Annotated[float, Field(..., gt=0, description='weight of patient in kgs.', examples=[70.9])]

    @computed_field
    @property
    def bmi(self) ->float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi
    

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi > 30:
            return "Obese"
    

@app.get("/")
def hello():
    return {"message": "Patient Management API."}

@app.get("/about")
def about():
    return {"message": "Fully functional api to manage your patient records."}

@app.get("/view") # gives all data at once
def view():
    data = loadData()

    return data


@app.get("/patient/{patientId}") # ID wise info retrival
def viewPatient(patientId: str = Path(..., description="ID of the patient in the DB", examples=["P001"])):
    # load all the patient
    data = loadData()
    if patientId in data:
        return data[patientId]
    raise HTTPException(404, "Patient Not Found!")


@app.get("/sort")
def sortPatients(sortby: str = Query('name', description="Sort on the basis of height, weight, bmi."), order: str = Query('asc', description="Sort by asc or desc order.")):
    validFields = ['name', 'height', 'weight', 'bmi']
    validOrders = ['asc', 'desc']

    if sortby not in validFields:
        raise HTTPException(400, f"Invalid field selected from {validFields}")
    
    if order not in validOrders:
        raise HTTPException(400, "Invalid order to sort.")
    

    data = loadData()

    sortOrder = True if order == 'desc' else False

    sortedData = sorted(data.values(), key=lambda x: x.get(sortby, 0), reverse=sortOrder)

    return sortedData


@app.post("/create")
def createPatient(patient: Patient):
    # load existing data
    data = loadData()

    if patient.id in data:
        raise HTTPException(400, "Patient already exists.")
    
    # new patient add to the databse
    data[patient.id] = patient.model_dump(exclude=["id"])

    # save into the json file
    saveData(data)

    return JSONResponse(status_code=201, content={"message": "Patient created successfully."})


