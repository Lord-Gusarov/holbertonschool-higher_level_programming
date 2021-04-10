#!/bin/bash
# Sends a POST request to the passed URL. Sents two variables in the resquest
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
