import json
try:
    with open("b.json", "r") as f:
        data = json.load(f)
        print("Read from b.json:", data)
except Exception as e:
    print("Could not read b.json:", str(e))
