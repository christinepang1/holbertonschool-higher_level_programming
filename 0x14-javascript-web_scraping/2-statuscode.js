#!/usr/bin/node
const request = require('request');
const input = process.argv[2];

request.get(input, (err, response) => {
  if (err) {
    console.log(err);
  }
  console.log('code:', response.statusCode);
});
