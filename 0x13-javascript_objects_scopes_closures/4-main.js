#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

const r2 = new Rectangle(0, 3);
console.log('\nNormal:');
r2.print();

console.log('Double:');
r2.double();
r2.print();

console.log('Rotate:');
r2.rotate();
r2.print();
