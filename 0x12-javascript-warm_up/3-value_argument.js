#!/usr/bin/node
const input = process.argv;
const inputs = input.length;
if (inputs === 2) {
  console.log('No argument');
} else {
  console.log(input[2]);
}
