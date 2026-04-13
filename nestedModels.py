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

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pinCode)