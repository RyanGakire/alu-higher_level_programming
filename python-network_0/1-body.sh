#!/bin/bash
# Takes a URL, sends a GET request, and displays the body only for a 200 status code response
curl -s -L -f "$1"
