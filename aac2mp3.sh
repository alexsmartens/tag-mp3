#!/bin/bash

DIR=./music/

NEW=music_mp3
mkdir $NEW

for f in $DIR*; do
  NAME=${f##*.*/}
  echo "/$NEW/${NAME%.*}.mp3"
  avconv -i "${f}" "./$NEW/${NAME%.*}.mp3"
done
