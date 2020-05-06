#!/usr/bin/node
let input = process.argv[2];
if (!parseInt(input)) {
  console.log('Missing number of occurences');
}
while (input > 0) {
  console.log('C is fun');
  input--;
}
