from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict, Annotated, Optional


class Patient(BaseModel):
    name : str
    age: int
    email: EmailStr
    married : Optional[bool] = None
    weight : float
    allergies : List[str]
    contactDetails : Dict[str, str]

    @field_validator('email')
    @classmethod
    def emailValidator(cls, value):
        validDomains = ['hdfc.com', 'icici.com']
        domainName = value.split('@')[-1]

        if domainName not in validDomains:
            raise ValueError("Not a valid domain.")
        
        return value

def updatePatientDetail(patient: Patient):
    print(patient.name)


patientInfo = {"name": "nitish", "email": "abc@hdfc.com", "age": 30, "weight": 45.8, "allergies":['pollen', 'dust'], "contactDetails":{ "Phone":"980123456"}}

patient1 = Patient(**patientInfo)

updatePatientDetail(patient1)

