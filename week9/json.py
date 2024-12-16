import json

with open ('data.json' , 'r') as file:
    python_dict = json.load(file)

python_dict = {'name': 'Jen', 'age': 21}
with open('output.json', 'w') as file:
    json.dump(python_dict, file)

