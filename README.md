# bg-words-dict

Списък с думи на български език.

## Генериране

Зависимости:

* wget
* sed
* unzip
* awk
* hunspell
* hunspell-bg

## Автоматично

```bash
./update.sh
```

## Ръчно

За генериране на списъка:

```bash
wget https://github.com/chitanka/content-text/archive/master.zip
unzip -p master.zip | sed "s/[^а-я^А-Я]/\n/g" | sed "/^.{,1}$/d" | awk '{print tolower($0)}' | sort -u > dict.txt
```

За генериране на списъка с валидните думи е използван `hunspell`:

```bash
hunspell -d bg_BG -G dict.txt | sort -u > dict.spellchecked.txt
```

Използван е корпус от https://github.com/chitanka/content-text.
