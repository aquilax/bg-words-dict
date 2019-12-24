import sys
import aspell

LANG = 'bg';

def main(filename):
    speller = aspell.Speller('lang', LANG)
    buffersize = 2**16
    with open(filename) as f:
        while True:
            lines_buffer = f.readlines(buffersize)
            if not lines_buffer:
                break
            for line in lines_buffer:
                word = line.strip()
                if speller.check(word):
                    print(word)


if __name__ == "__main__":
    main(sys.argv[1])
