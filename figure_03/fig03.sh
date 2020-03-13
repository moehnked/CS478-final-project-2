#!/bin/bash

#SECTION:
#Manipulating Delimiters

# from the linux man pages: tr - translate or delete characters
# it can be tricky to understand what is going on at first, but the tr command in Collin's code has two sets provided as arguments
# 'dog' and 'bat'
# tr will replace any instance of dog with bat
# because 'god' is 'dog' backwards, it gets replaced with 'tab' which is 'bat' backwards
echo 'dog cat god' | tr 'dog' 'bat'
printf "\n"
#here the -s option replaces an entire sequence of repeated characters with the set specified
echo 'a||b|c' | tr -s '|'