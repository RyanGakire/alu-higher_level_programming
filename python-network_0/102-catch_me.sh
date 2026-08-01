#!/bin/bash
# Makes a request to /catch_me, following redirects, so the server answers "You got me!"
curl -s -L -X PUT -H "X-School-User-Id: 98" -H "User-Agent: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me?user_id=98"
