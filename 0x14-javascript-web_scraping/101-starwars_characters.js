#!/usr/bin/node
const request = require('request');

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error) {
        resolve(JSON.parse(body).name);
      } else {
        reject(error);
      }
    });
  });
}

async function main (film) {
  for (const charAPI of film.characters) {
    const res = await doRequest(charAPI);
    console.log(res);
  }
}

const films = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(films, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const film = JSON.parse(body);
  main(film);
});
