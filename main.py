from fastapi import FastAPI
from dataLoader import loadData

app = FastAPI()



@app.get("/")
def hello():
    return {"message": "Patient Management API."}

@app.get("/about")
def about():
    return {"message": "Fully functional api to manage your patient records."}

@app.get("/view")
def view():
    data = loadData()

    return data