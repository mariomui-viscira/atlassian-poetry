#! /bin/sh

poetry export --without-hashes | while IFS=  read -r line; do  echo $line | sed -e 's/;.*$//' ; done