
const fs = require('fs');
try {
  const raw = fs.readFileSync("a.json");
  const data = JSON.parse(raw);
  console.log("Read from a.json:", data);
} catch (e) {
  console.error("Could not read a.json:", e.message);
}
