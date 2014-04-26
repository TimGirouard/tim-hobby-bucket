#!/bin/bash

ls -lS --time-style=long-iso | awk 'BEGIN {getline;getline;name1=$8;size=$5} \
{name2=$8;command=print name1 | md5sum | getline; csum1=$1;command=print name2 | md5sum | getline; csum2=$1;}'

#{name2=$8;if (size==$5) {print size;print $5};size=$5;name1=name2}

#{print name1;print name2}
