#!/usr/bin/node

const argFirst = parseInt(process.argv[2]);
if (isNaN(argFirst)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argFirst);
}
