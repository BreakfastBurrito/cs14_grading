#!/bin/bash

if [ "$#" -eq 0 ] || [ "$#" -gt 1 ]
then
  echo "This script requires a single argument"
  exit 1
elif [ -f $1 ]
then
  echo "This script takes only a directory as an argument"
  exit 2
fi

mkdir $1/build

cp cs14_grading/hw1/tests_MyList.py $1/build
cp cs14_grading/hw1/{CmakeLists.txt,MyGradingList.cpp} $1

cd $1/build
cmake -DPYTHON_LIBRARY=/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/libpython2.7.dylib ../
make
echo $? >> ../../passed

py.test -v tests_MyList.py | cat
