#!/bin/bash

# Prompt the user to enter a number
read -p "Enter a number: " num

# Loop until the number is greater than 10
while [ $num -le 10 ]
do
    echo "The number is less than or equal to 10."
    read -p "Enter another number: " num
done

echo "The number is greater than 10."

echo "Done."

