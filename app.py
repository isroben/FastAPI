from fastapi import FastAPI
import pydantic


app = FastAPI()

@app.get("/")
def helloworld():
    return {"message" : "Hello world"}