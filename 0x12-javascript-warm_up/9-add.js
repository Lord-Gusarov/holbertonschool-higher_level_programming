#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2, 4);
args[0] = parseInt(args[0]); args[1] = parseInt(args[1]);

console.log(add(args[0], args[1]));
