#!/usr/bin/node

const args = process.argv.slice(2);
let idx, biggest;
let second = 0;

if (args.length > 1) {
  for (idx = 0; idx < args.length; idx++) {
    args[idx] = parseInt(args[idx]);
  }
  biggest = second = Math.min(...args);

  for (idx = 0; idx < args.length; idx++) {
    if (args[idx] >= biggest) {
      second = biggest;
      biggest = args[idx];
    }
  }
}

console.log(second);
