#!/usr/bin/node

// Import the 'fs' module to handle file system operations
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Check if a file path is provided
if (!filePath) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

// Read the file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // If an error occurs, print the error object
    console.error(err);
  } else {
    // If successful, print the file content
    console.log(data);
  }
});
