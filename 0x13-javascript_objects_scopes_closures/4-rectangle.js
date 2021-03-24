#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Prints a Rectangle using the char 'X'
  print () {
    for (let i = this.height; i--;) {
      console.log('X'.repeat(this.width));
    }
  }

  // Exchanges the widht and height of a Rectangle
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // Doubles the height and width of a Rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
