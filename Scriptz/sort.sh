#!/bin/bash
#Filename: sort.sh
sort -C asorted.txt ;
if [ $? -eq 0 ]; then
	echo Sorted;
else
	echo Unsorted;
fi
