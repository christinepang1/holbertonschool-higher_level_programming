#!/usr/bin/node
const input = process.argv[2];
let i = 0;
const size = parseInt(input);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
