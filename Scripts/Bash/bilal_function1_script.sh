#!/bin/bash

# Define a function called "sum"
function sum {
    local a=$1
    local b=$2
    local total=$((a + b))
    echo $total
}

# Call the "sum" function with arguments 2 and 3, and store the result in a variable
result=$(sum 2 3)

echo "2 + 3 = $result"

