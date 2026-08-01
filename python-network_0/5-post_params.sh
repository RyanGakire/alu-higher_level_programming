#!/bin/bash
# Sends a POST request to the URL with the parameters email and subject, and displays the body
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
