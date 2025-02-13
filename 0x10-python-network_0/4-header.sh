#!/bin/bash
# Script that sends GET request with custom header and displays response body
curl -s -H "X-School-User-Id: 98" "$1"
