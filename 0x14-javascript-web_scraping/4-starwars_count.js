#!/usr/bin/node
const request = require('request');
const input = process.argv[2];

request.get(input, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  let i = 0;
  let count = 0;
  const key = JSON.parse(body).results;
  while (key[i]) {
    if (key[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
    i++;
  }
  console.log(count);
});
