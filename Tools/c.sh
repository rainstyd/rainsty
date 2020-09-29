#!/bin/bash
cat a.txt |awk -F '`' '{print $2 ","}'
# cat a.txt |awk -F '`' '{print $2 " zj_column_" $2 ","}'
# cat a.txt |awk -F '`' '{print "'\''" "zj_column_" $2 "'\''" ","}'
cat a.txt |awk -F '`' '{print $2}'|xargs|awk '{gsub(/ /, ", ");print}'
cat a.txt |awk -F '`' '{print $2"=values("$2")"}'|xargs|awk '{gsub(/ /, ", ");print}'
cat a.txt |awk -F '`' '{print $2}'|xargs|awk '{gsub(/ /, "\)s\, \%\(");print "\%(" $0 "\)s"}'
cat a.txt |awk -F '`' '{print $2 "=" $2}' |xargs |awk '{gsub(/ /, "\)s\ and ");print $0 "\)s"}'|awk 'gsub(/=/, "=\%\("){print $0}'
# cat a.txt |awk -F '`' '{print $2 ","}'| awk -F ',' '{print $1 " = scrapy.Field()"}'
# cat a.txt |awk -F '`' '{print "item[\"" $2 "\"] = 111111"}'
cat a.txt |awk -F '`' '{print $2}'|xargs|awk 'gsub(/ /, "\", \""){print "\"" $0 "\""}'

