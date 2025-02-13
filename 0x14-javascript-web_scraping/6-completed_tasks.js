#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Check if the API URL is provided
if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <API-URL>');
  process.exit(1);
}

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurs, print the error
    console.error(error);
  } else if (response.statusCode !== 200) {
    // If the response status code is not 200, print an error
    console.error(`Error: Status code ${response.statusCode}`);
  } else {
    // Parse the response body and count completed tasks by user ID
    const tasks = JSON.parse(body);
    const completedTasks = {};

    tasks.forEach((task) => {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    });

    console.log(completedTasks);
  }
});
