from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pinCode: str

class Patient(BaseModel):
    name : str
    gender : str
    age : int
    address: Address


addressDict = {'city': 'Kathmandu', 'state': 'Bagmati', 'pinCode': '45100'}

address1 = Address(**addressDict)

patientDict = {'name': 'Roben', 'gender': 'Male', 'age': 30, 'address': address1}

patient1 = Patient(**patientDict)

temp = patient1.model_dump(include=['name', 'age'])
temp = patient1.model_dump(exclude=['name', 'age'])

print(temp)
print(type(temp))