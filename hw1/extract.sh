#!/bin/bash

for filename in *
do
  new_dir=$(echo $filename | grep '[^_][A-Za-z]*[^_][0-9]\{3\}' -o)
  mkdir -p $new_dir/build
  tar -zxvf "$filename" -C $new_dir
  mv ./*$new_dir* $new_dir
done

#Fixes class getter
grep -rl -v "char operator\[\]" ./* | grep -v Homework | xargs -I{} sed -i '' s/char\&/char/ {}

#Makes extensions uniform
find . -iname "*.H" -exec bash -c 'mv "$0" "${0%\.H}.hpp"' {} \;
find . -iname "*.h" -exec bash -c 'mv "$0" "${0%\.h}.hpp"' {} \;
