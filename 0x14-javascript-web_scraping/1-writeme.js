#!/usr/bin/node
const fs = require('fs');

const filename = process.argv[2];
const data = process.argv[3];

fs.writeFile(filename, data, err => {
  if (err) {
    console.error(err);
  }
});
