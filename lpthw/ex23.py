import sys
from os.path import exists
from codecs import decode

script, input_encoding, error, mode = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        if mode == "r" or "rr":
            encoded_lines.append(reverseEncoding(line, encoding, errors))
            encoded_lines.append("\n")
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    if mode == "rr":
        raw_bytes = decode(next_lang, "hex")
    else:
        raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


def reverseEncoding(line, encoding, errors):
    next_lang = line.strip()
    if mode == "r":
        raw_bytes = next_lang.encode(encoding, errors=errors).hex()
        return raw_bytes
    elif mode == "rr":
        string = decode(next_lang, "hex").decode(encoding, errors=errors)
        return string


if not(exists('languages.txt')):
    print("`languages.txt` does not exist!\nPlease download it from \"https://learnpythonthehardway.org/python3/languages.txt\"")
    exit(1)

languages = open("languages.txt", "r+", encoding="utf-8")
encoded_lines = []

main(languages, input_encoding, error)
if mode == "r" or "rr":
    languages.seek(0)
    languages.truncate()
    languages.writelines(encoded_lines)
languages.close()
