#!/usr/bin/node

exports.esrever = function (list) {
  var output = [];
  while (list.length) {
    output.push(list.pop());
  }

  return output;
};
