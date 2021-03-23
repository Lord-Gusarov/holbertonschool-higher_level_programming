#!/usr/bin/node

exports.callMeMoby = function (x, aFunction) {
  while (x > 0) {
    aFunction();
    x--;
  }
};
