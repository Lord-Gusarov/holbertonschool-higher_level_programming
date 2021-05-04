#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
