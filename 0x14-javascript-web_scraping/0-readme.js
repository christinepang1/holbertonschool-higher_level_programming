#!/usr/bin/node
const fs = require('fs');
const input = process.argv[2];

fs.readFile(input, (err, data) => {
  if (err) console.log(err);

  console.log(data);
});
