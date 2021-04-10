#!/bin/bash
# Takes in a URL as an argument, and displays the body of the response. A header variable X-HolbertonSchool-User-Id must be sent with the value 98
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
