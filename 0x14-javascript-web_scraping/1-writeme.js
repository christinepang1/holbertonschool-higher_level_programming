#!/usr/bin/node
const fs = require('fs');
const input = process.argv[2];
const text = process.argv[3];

fs.writeFile(input, text, 'utf8', err => {
  if (err) console.log(err);
});
