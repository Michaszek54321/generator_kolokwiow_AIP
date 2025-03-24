'''
Moduł `generator` będzie głównym modułem generującym kolokwia.
'''
import json
json_data = json.load(open('kolos.ipynb'))

print(json_data["cells"][0]["source"])