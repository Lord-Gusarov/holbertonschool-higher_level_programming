#!/usr/bin/node

// Reverses a list without using the built-in method reverse
exports.esrever = function (list) {
  const revList = [];
  for (let i = list.length; i--;) {
    revList.push(list[i]);
  }
  return revList;
};
