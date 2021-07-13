#!/bin/bash
if [[ "$#" != 1 ]]; then
  echo "Usage: $0 <branch>"
  exit -1
fi
echo "Size before cleaning:" $(du -sh .)
rm -rf __pycache__
echo "Size after cleaning:" $(du -sh .)
git add .
git commit -m "checkpoint commit"
git push origin $1
