#!/bin/bash

x=$1
nn=$(echo $x| sed "s|rules_2|rules_2_small|g")
convert -resize x500 -quality 90 "$x" "$nn"

