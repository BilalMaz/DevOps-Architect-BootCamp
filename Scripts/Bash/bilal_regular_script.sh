#!/bin/bash

# Define a variable containing a sample text
text="hello world! this is a sample text."

# Use the "grep" command with a regular expression to find all occurrences of the word "hello"
matches=$(echo "$text" | grep -o "hello")

# Print the matches to the console
echo "$matches"

