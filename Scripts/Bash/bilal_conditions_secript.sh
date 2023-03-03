#!/bin/bash

# Prompt the user to enter a number
read -p "Enter a number: " num

# Check if the number is greater than 10
if [ $num -gt 10 ]; then
    echo "The number is greater than 10."
fi

# Check if the number is less than or equal to 10
if [ $num -le 10 ]; then
    echo "The number is less than or equal to 10."
fi

