#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
let output = 0;

if (args.length > 1) {
  output = args.sort((a, b) => (b - a))[1];
}
console.log(output);
