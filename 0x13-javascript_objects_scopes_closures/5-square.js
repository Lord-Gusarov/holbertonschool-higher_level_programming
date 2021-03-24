#!/usr/bin/node

// Inherits from Rectangle class in module '4-rectangle.js'
class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
