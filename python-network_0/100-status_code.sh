#!/bin/bash
# Sends a request to the URL passed as an argument and displays only the response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
