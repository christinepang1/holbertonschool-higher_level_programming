#!/usr/bin/node
const fs = require('fs');
const input = process.argv[2];

fs.readFile(input, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
    }
  console.log(data);
});
