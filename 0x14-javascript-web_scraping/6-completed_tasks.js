#!/usr/bin/node
const request = require('request');
const input = process.argv[2];
const dict = {};

request(input, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed) {
        if (!(data[i].userId in dict)) {
          dict[data[i].userId] = 0;
        }
        dict[data[i].userId] += 1;
      }
    }
    console.log(dict);
  }
});
