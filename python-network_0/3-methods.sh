#!/bin/bash
# Takes a URL and displays all the HTTP methods the server will accept for it
curl -s -i -X OPTIONS "$1" | grep -i '^Allow:' | cut -d ' ' -f 2-
