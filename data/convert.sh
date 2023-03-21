#!/bin/bash

for x in rules_2/*/; do
    echo $x
    nn=$(echo $x| sed "s|rules_2|rules_2_small|g")
    echo $nn
    mkdir -p "$nn"
done


find rules_2/*/ -name "*.jpg" | xargs -i -P 120 ./convert_img.sh {}

