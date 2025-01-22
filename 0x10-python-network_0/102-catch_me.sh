#!/bin/bash
# Script that makes request to catch_me and gets "You got me!" response
curl -s -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
