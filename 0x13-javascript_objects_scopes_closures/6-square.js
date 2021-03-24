#!/usr/bin/node

// Inherits from Square Rectangle class in module '5-square.js'
class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  // Prints a Square using the given char or if no char is specified
  // it defauls to the parent's class print()
  charPrint (c = 'X') {
    for (let i = this.height; i--;) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
