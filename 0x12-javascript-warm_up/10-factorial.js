#!/usr/bin/node

function factorial (n) {
  if (n <= 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}

let num = parseInt(process.argv[2]);
if (isNaN(num)) {
  num = 1;
}
console.log(factorial(num));
