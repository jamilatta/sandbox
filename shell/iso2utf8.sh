#!/bin/bash

if [ $# -ne 2 ]
then
    echo "Invalid Argument Count"
    echo "folder xxx(extension of file)"
    echo "Example:"
    echo "./iso2utf8.sh teste html"
    exit
fi

for files in $1*.$2
do
  iconv -f ISO-8859-1 -t UTF-8 "$files" > "${files%.$2}-utf8.$2"
done
