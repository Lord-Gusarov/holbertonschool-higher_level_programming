#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(x => x === searchElement ? count++ : '');
  return count;
};
