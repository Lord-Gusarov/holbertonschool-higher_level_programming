#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Prints a rectangle using the char 'X'
  print () {
    for (let i = this.height; i--;) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
