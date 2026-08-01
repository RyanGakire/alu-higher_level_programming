#!/bin/bash
# Sends a JSON POST request to the URL, with the file as body, and displays the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
