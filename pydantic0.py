from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of Patient")]
    email: EmailStr # Custom datatypes
    age: int = Field(gt=12, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    allergies: Optional[List[str]]  = Field(max_length=5) # Making the field optional
    contact: Dict[str, str]



patient_info = {"name": "nitish", "email": "abc@gmail.com", "age": 30, "weight": 45.8, "allergies":['pollen', 'dust'], "contact":{ "Phone":"980123456"}}

def insertPatientData(patient: Patient):
    print(patient.name)
    print(patient.age)

def updatePatientData(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact)


patient1 = Patient(**patient_info)

insertPatientData(patient1)
updatePatientData(patient1)
