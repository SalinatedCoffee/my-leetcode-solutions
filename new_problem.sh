#!/usr/bin/env bash

# print usage
if [[ ( $@ == "--help" ) || ( $@ == "-h" ) ]]
then
  echo "Usage: $0 [number] [difficulty] [title] [language]"
  exit 0
fi

# check supplied arguments
case $# in
  3)
    echo "Language not specified, assuming Python 3"
    lang="Python3"
  ;;
  4)
    lang=$4
  ;;
  *)
    echo "Expected 3-4 arguments, got $# instead"
    echo "Usage: $0 [number] [difficulty] [title] [language]"
    exit 0
  ;;
esac

padded=$1
if [ ${#1} -ne 4 ]
then
  pad=$((4-${#1}))
  for ((i=0; i<pad; i++))
  do
    padded="0$padded"
  done
fi

path="$lang/$padded. ($2) $3"
mkdir -p "$path"
touch "$path/solution.py"
cp README_template.md "$path/README.md"
echo "$path"

