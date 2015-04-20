#!/bin/bash

rm ./*.txt

for filename in *
do
  new_dir=$(echo $filename | grep '[^_][A-Za-z]*[^_][0-9]\{3\}' -o)

  if [[ $filename =~ \.tar$  ]];
  then
    mkdir -p $new_dir/build
    tar -xvf "$filename" -C $new_dir
  elif [[ $filename =~ \.tar.gz$  ]];
  then
    mkdir -p $new_dir/build
    tar -zxvf "$filename" -C $new_dir
  elif [[ $filename =~ \.h|.H$  ]];
  then
    mkdir -p $new_dir/build
    mv $filename $new_dir/MyList.hpp
  else
    echo "****ERROR*****"
    echo $filename
    echo "did not match any extension"
  fi
done

#Fixes for sed osx
export LC_CTYPE=C
export LANG=C

#Fixes class getter
grep -rl -v "char& operator\[\]" ./* | grep -v cs14_grading | xargs -I{} sed -i '' s/char\&/char/ {}

#Makes extensions uniform
find . -iname "*.H$" -exec bash -c 'mv "$0" "${0%\.H}.h"' {} \;
