#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const input = process.argv[2];
const filename = process.argv[3];

request(input, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filename, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
