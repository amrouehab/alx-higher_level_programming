#!/bin/bash
# Script that sends JSON POST request with contents of a file
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
