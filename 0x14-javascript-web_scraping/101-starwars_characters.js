#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Check if the movie ID is provided
if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <movie-id>');
  process.exit(1);
}

// Define the Star Wars API endpoint
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurs, print the error
    console.error(error);
  } else if (response.statusCode !== 200) {
    // If the response status code is not 200, print an error
    console.error(`Error: Status code ${response.statusCode}`);
  } else {
    // Parse the response body and fetch character names in order
    const characters = JSON.parse(body).characters;
    const characterNames = [];

    let count = 0;
    characters.forEach((characterUrl, index) => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          characterNames[index] = JSON.parse(body).name;
          count++;

          // Print names when all characters are fetched
          if (count === characters.length) {
            characterNames.forEach((name) => console.log(name));
          }
        }
      });
    });
  }
});
