#!/usr/bin/node

const list = require('./100-data.js').list;
console.log(list);
let idx = 0;
console.log(list.map(x => x * idx++));
