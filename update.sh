#!/bin/bash

set -e

if [ ! -f master.zip ]; then
    wget https://github.com/chitanka/content-text/archive/master.zip
fi

unzip -p master.zip | sed "s/[^а-я^А-Я]/\n/g" | sed "/^.{,1}$/d" | awk '{print tolower($0)}' | sort -u > dict.txt
hunspell -d bg_BG -G dict.txt | sort -u > dict.spellchecked.txt
