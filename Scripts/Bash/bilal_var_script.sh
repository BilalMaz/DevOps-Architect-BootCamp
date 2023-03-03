#!/usr/bin/env bash
# Note that spaces cannot be used around the `=` assignment operator
whom_variable="Bilal learning_scripting"
# Use printf to safely output the data
printf "Hello, %s\n" "$whom_variable"
#> Hello, World
