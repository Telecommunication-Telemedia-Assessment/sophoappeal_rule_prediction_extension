#!/bin/bash

for x in *.ldjson; do
    echo "$x"
    ./download_list.sh "$x"
    ./duplicates.py "$(basename $x .ldjson)" --del
done