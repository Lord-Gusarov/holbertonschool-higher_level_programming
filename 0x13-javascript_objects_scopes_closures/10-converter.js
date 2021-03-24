#!/usr/bin/node

exports.converter = function (base) {
  return function (toConvert) {
    return toConvert.toString(base);
  };
};
