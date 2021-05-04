#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  // Charcater Wedge Antilles
  const antilles = 'https://swapi-api.hbtn.io/api/people/18/';
  for (const film of films) {
    for (const character of film.characters) {
      if (character.localeCompare(antilles) === 0) {
        count++;
      }
    }
  }
  console.log(count);
});
