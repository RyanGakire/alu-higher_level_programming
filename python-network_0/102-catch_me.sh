#!/bin/bash
# Makes a request to /catch_me, following redirects, so the server answers "You got me!"
curl -s -L -X PUT -H "X-School-User-Id: 98" -H "X-HolbertonSchool-User-Id: 98" 0.0.0.0:5000/catch_me
