import json

try:
    with open('sample2.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        print(data)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)