#!/bin/bash
# Sends a GET request to the URL with the header X-HolbertonSchool-User-Id set to 98
curl -s -H "X-HolbertonSchool-User-Id: 98" -H "X-School-User-Id: 98" "$1"
