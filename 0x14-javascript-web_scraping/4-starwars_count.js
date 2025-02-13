#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Check if the API URL is provided
if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API-URL>');
  process.exit(1);
}

// Define the character ID for Wedge Antilles
const wedgeAntillesId = 18;

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurs, print the error
    console.error(error);
  } else if (response.statusCode !== 200) {
    // If the response status code is not 200, print an error
    console.error(`Error: Status code ${response.statusCode}`);
  } else {
    // Parse the response body and count movies where Wedge Antilles appears
    const films = JSON.parse(body).results;
    const count = films.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)
    ).length;
    console.log(count);
  }
});
