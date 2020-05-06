#!/usr/bin/node
let x;
let num;
const inputs = process.argv;
if (inputs.length > 2) {
  num = parseInt(inputs[2]);
  if (!isNaN(num)) {
    x = 'My number: ' + String(num);
    console.log(x);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
