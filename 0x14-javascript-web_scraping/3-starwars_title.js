#!/usr/bin/node
const request = require('request');
const input = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + input, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const key = JSON.parse(body);
  console.log(key.title);
});
