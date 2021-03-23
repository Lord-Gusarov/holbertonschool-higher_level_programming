#!/usr/bin/node

const args = process.argv.slice(2);
let idx, biggest, second;

if (args.length <= 1) {
  second = 0;
} else {
  for (idx = 0; idx < args.length; idx++) {
    args[idx] = parseInt(args[idx]);
  }
  biggest = second = args[0];

  for (idx = 1; idx < args.length; idx++) {
    if (args[idx] > biggest) {
      second = biggest;
      biggest = args[idx];
    }
  }
}

console.log(second);
