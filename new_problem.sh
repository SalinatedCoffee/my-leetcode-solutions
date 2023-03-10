#!/usr/bin/env bash

# TODO: Add support for adding new language to solved problem

# print usage
if [[ ( $@ == "--help" ) || ( $@ == "-h" ) ]]
then
  echo "Usage: $0 [number] [difficulty (E|M|H)] [title] [language (Python3|Java|MySQL)]"
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
    echo "Usage: $0 [number] [difficulty(E|M|H)] [title] [language (Python3|Java|MySQL)]"
    exit 0
  ;;
esac

if ! [[ "$2" == [EMH] ]]
then
  echo "Got $2 as difficulty, expected E(asy)|M(edium)|H(ard)"
  exit 0
fi

# pad left with 0 if problem number is smaller than 4 digits
padded=$1
if [ ${#1} -ne 4 ]
then
  pad=$((4-${#1}))
  for ((i=0; i<pad; i++))
  do
    padded="0$padded"
  done
fi

# get relative path to this script
top_path="$(dirname -- "${BASH_SOURCE[0]}")"

# construct path and set up problem directory
path="$top_path/Problems/$padded. ($2) $3/$lang"
mkdir -p "$path"

# change solution file extension based on supplied language
case $lang in
  "Python3")
    ext="py"
  ;;
  "Java")
    ext="java"
  ;;
  "MySQL")
    ext="sql"
  ;;
esac
touch "$path/solution.$ext"

# for now, add expanations for all languages other than Java
if ! [[ $ext == "java" ]]
then
  cp "$top_path/README_template.md" "$path/README.md"
fi
echo "$path"

