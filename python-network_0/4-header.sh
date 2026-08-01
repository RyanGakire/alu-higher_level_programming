#!/bin/bash
# Sends a GET request to the URL with the header X-HolbertonSchool-User-Id set to 98
curl -s -L -H "X-HolbertonSchool-User-Id: 98" "$1"
