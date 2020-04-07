#!/bin/bash
# Bash script that takes in a URL and gives you size
curl -ILs $1 | grep Content-Length | cut -d' ' -f2
