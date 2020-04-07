#!/bin/bash
# Takes in a URL, sends a GET request, and displays the body of the response
curl -s "$1" GET -H "X-HolbertonSchool-User-Id:98"
