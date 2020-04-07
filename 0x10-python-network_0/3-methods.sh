#!/bin/bash
# Bash script that takes in a URL and gives you size
curl -ILs $1 | grep Allow | cut -f2- -d' '
