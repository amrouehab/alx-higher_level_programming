#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    
    const fetchCharacter = (index) => {
      if (index < characters.length) {
        request(characters[index], (err, response, body) => {
          if (!err) {
            console.log(JSON.parse(body).name);
            fetchCharacter(index + 1);
          }
        });
      }
    };
    
    fetchCharacter(0);
  }
});
