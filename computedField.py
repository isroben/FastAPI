from pydantic import BaseModel, computed_field
from typing import List, Dict, Optional, Self

class Patient(BaseModel):
    name : str
    age : int
    email: str
    weight : float
    height: float
    married: bool
    allergies : List[str]
    contactDetails: Dict[str, str]

    
    @computed_field
    @property
    def BMI(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi
    

def UpdateInfo(patient: Patient):
    print("BMI", patient.BMI)

patientInfo = {"name": "nitish", "email": "abc@hdfc.com", "age": 80, "weight": 45.8, "height": 6.1, "married": True, "allergies":['pollen', 'dust'], "contactDetails":{ "Phone":"980123456"}}

patient1 = Patient(**patientInfo)


UpdateInfo(patient1)
