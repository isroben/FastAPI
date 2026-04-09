import json

def loadData():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data
