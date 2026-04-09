from fastapi import FastAPI, Path, HTTPException
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


@app.get("/patient/{patientId}") # ID wise info retrival
def viewPatient(patientId: str = Path(..., description="ID of the patient in the DB", example="P001")):
    # load all the patient
    data = loadData()
    if patientId in data:
        return data[patientId]
    raise HTTPException(404, "Patient Not Found!")