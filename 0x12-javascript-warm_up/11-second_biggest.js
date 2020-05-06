#!/usr/bin/node
const input = process.argv;
if (input.length <= 3) {
  console.log(0);
} else {
  const array = input.slice(2);
  const sorted = array.sort();
  console.log(array[sorted.length - 2]);
}
