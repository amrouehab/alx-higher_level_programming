#!/bin/bash
# Script that displays all HTTP methods the server accepts
curl -s -I -X OPTIONS "$1" | grep "Allow" | cut -d " " -f2-
