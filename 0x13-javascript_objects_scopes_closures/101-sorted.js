#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};
let k, v;
for (k in dict) {
  v = dict[k];
  v in newDict ? newDict[v].push(k) : newDict[v] = [k];
}
console.log(newDict);
