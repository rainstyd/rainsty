#!/bin/bash

cat b.txt |awk -F '#' '{print $2}'|xargs| awk 'gsub(/ /, "|"){print $ 0}'
cat b.txt |awk -F '\[' '{print $2}'|awk -F '\]' '{print $1}'|xargs| awk 'gsub(/ /, "\", \""){print "[\"" $0 "\"]"}'

