#!/usr/bin/node

// Reverses a list without using the built-in method reverse
exports.esrever = function (list) {
  let rev_list = new Array();
  for (let i = list.length; i--;) {
    rev_list.push(list[i]);
  }
  return rev_list;
}
