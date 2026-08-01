#!/bin/bash
# Makes a request to /catch_me, following redirects, so the server answers "You got me!"
curl -s -L -X PUT 0.0.0.0:5000/catch_me
