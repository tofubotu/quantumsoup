
const fs = require('fs');
const data = {
  name: "Bob",
  age: 42,
  is_admin: false,
  skills: ["JavaScript", "Docker"]
};

fs.writeFileSync("b.json", JSON.stringify(data, null, 2));
console.log("b.json written by JavaScript");
