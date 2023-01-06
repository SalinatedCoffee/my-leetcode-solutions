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
    echo "Language not specified, defaulting to Python 3"
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

path="$lang/$1. ($2) $3"
mkdir -p "$path"
touch "$path/solution.py"
cp README_template.md "$path/README.md"
