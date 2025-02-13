#!/usr/bin/node

// Import the 'fs' module to handle file system operations
const fs = require('fs');

// Get the file path and string to write from the command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Check if both file path and content are provided
if (!filePath || !content) {
  console.error('Usage: ./1-writeme.js <file-path> <string-to-write>');
  process.exit(1);
}

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // If an error occurs, print the error object
    console.error(err);
  }
});
