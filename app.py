from fastapi import FASTAPI
import pydantic


app = FASTAPI()

app.get("/")

def helloworld():
    return {"message" : "Hello world"}