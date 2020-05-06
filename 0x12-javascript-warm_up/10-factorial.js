#!/usr/bin/node
function factorial (num) {
  if (isNaN(num)) {
    return (1);
  } else if (num === 0) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
let input = process.argv[2];
input = parseInt(input);
console.log(factorial(input));
