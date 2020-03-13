#!/bin/bash

#SECTION:
#Finding a String


#the grep command prints lines matching a pattern - it stands for Global Regular Expression Print
#the output of the first search for '10.16' in the file 'http_example.txt' from Collins is then piped to another grep command which filters the results for a timestamp matching '10:16'
#chaining grep commands together is one technique for filtering large text files to find relevant information
grep 10.16 ../source_files/http_example.txt | grep '10:16'
printf "\n"
# the -v option inverts the filter, printing non matching results, which is then piped into the head command
# head takes a number as an argument which specifies how many lines from the start of the result to print
#in this case, head -1 means only print the first line
grep 10.16 ../source_files/http_example.txt | grep -v '10:16' | head -1
printf "\n"

# the . in grep is actually a wildcard operator. if one wishes to search for patterns which include the '.' character,
# one must specify the pattern as a string and escape the . with the \ operator
grep '10\.16' ../source_files/http_example.txt | head -1