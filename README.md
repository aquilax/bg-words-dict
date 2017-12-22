# bg-words-dict

Списък думи кирилица

За да генерирате списъка:

```
wget https://github.com/chitanka/content-text/archive/master.zip
unzip -p content-text-master.zip | sed "s/[^а-я^А-Я]/\n/g" | awk '{print tolower($0)}' | sort -u > dict.txt
```

За генериране на списъка с валидните думи е използван `aspell`:
```
python sift.py dict.txt > dict.spellchecked.txt
```

Използван е корпус от https://github.com/chitanka/content-text.
