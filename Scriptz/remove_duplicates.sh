#!/bin/bash
#Filename: remove_duplicates.sh
#Desc: Find an remove duplicate files, keeping one sample of each file.

ls -ls --time-style=long-iso | awk 'BEGIN {
	getline; getline;
	name1=$9; size=$6
}
{
	name2=$9;
	if (size==$6)
	{
		"md5sum "name1 | getline; csum1=$1;
		"md5sum "name2 | getline; csum2=$1;
		if ( csum1==csum2 )
		{
			print name1; print name2
		}
	};

	size=$6; name1=name2;
}' | sort -u > duplicate_files

cat duplicate_files | xargs -I {} md5sum {} | sort | uniq -w 32 | awk '{ print "^"$2"$" }' | sort -u > duplicate_sample

echo Removing..
comm duplicate_files duplicate_sample -2 -3 | tee /dev/stderr | xargs rm
echo Removed duplicated files successfully.
