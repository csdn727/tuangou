#!/bin/bash

apis=`pcregrep '^\s+api\s*=\s*' * |awk '{print $(NF)}' |xargs`

getDomain(){
    echo "$1"|pcregrep -o '(?<=http://)[^/]+' |awk -F'.' '{print $(NF-1)}'
}
for api in $apis
do
    wget "$api" -O "`getDomain $api`".xml &
done
