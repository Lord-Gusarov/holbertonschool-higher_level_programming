#!/usr/bin/node
const request = require('request');

const films = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(films, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const film = JSON.parse(body);
  for (const charAPI of film.characters) {
    request(charAPI, (err, res, body) => {
      if (err) {
        console.error(err);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
