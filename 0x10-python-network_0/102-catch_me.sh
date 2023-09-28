#!/bin/bash

# Use curl to send a GET request to the server and follow redirects
curl -sLX GET 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool"

