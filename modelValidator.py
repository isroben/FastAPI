from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional


class Patient(BaseModel):
    name : str
    age: int
    email: EmailStr
    married : Optional[bool] = None
    weight : float
    allergies : List[str]
    contactDetails : Dict[str, str]

    @model_validator(mode='after')
    def validateEmergencyContact(cls, model):
        if model.age > 60 and 'emergency' not in model.contactDetails:
            raise ValueError("Person gt 60 must have emergency contacts.")
        return model


patientInfo = {"name": "nitish", "email": "abc@hdfc.com", "age": 80, "weight": 45.8, "allergies":['pollen', 'dust'], "contactDetails":{ "Phone":"980123456"}}
