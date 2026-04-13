import json

def loadData():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

def saveData(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)
