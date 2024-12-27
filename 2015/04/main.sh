#!/bin/bash
key=$(cat input.txt)

find_number() {
    number=0
    while true; do
        result=$(echo -n "${key}${number}" | md5sum)
        if [[ $result == $1* ]]; then
            echo $number
            break
        fi
        ((number++))
    done
}

time echo "Part1: $(find_number 00000)"
time echo "Part2: $(find_number 000000)"