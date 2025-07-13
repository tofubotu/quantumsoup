
import json
data = {
    "name": "Alice",
    "age": 30,
    "is_admin": True,
    "skills": ["Python", "Node.js"]
}
with open("a.json", "w") as f:
    json.dump(data, f, indent=2)

print("a.json written by Python")
