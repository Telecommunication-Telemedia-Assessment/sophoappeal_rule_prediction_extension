#!/bin/bash
list="$1"
dir=$(basename "$list" .ldjson)

cat "$list" | jq .url_o | sort | uniq | xargs -P40 -i wget {} --directory-prefix="$dir" -c
