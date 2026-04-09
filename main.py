from fastapi import FastAPI
from dataLoader import loadData

app = FastAPI()



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


@app.get("/patient/{patientId}")
def viewPatient(patientId: str):
    # load all the patient
    data = loadData()
    if patientId in data:
        return data[patientId]
    return {"error":"Patient Not Found!"}