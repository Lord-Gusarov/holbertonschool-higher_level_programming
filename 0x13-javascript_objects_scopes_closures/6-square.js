#!/usr/bin/node

// Inherits from Rectangle class in module '4-rectangle.js'
class Square extends require('./4-rectangle') {
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
