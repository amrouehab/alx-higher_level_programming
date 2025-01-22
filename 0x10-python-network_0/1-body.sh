#!/bin/bash
# Script that displays body of 200 status code response from a URL
curl -s -w '%{http_code}' "$1" -o /tmp/body && [ "$(cat /tmp/body)" = "200" ] && curl -s "$1"
