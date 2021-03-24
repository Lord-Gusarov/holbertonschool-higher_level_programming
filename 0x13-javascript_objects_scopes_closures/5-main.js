#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

console.log('\n< Nothing should follow >')
const s2 = new Square(-4);
s2.print();
s2.double();
s2.print();

