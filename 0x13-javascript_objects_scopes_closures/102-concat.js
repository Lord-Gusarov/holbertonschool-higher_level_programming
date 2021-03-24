#!/usr/bin/node

const fs = require('fs');
const files = process.argv.slice(2);

try {
  const content = fs.readFileSync(files[0]) +
    fs.readFileSync(files[1]);
  fs.writeFileSync(files[2], content);
} catch {
  console.log('Failed to concatenate the Files');
}
