#! /usr/bin/env python3

import os
import re
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py input_file output_file")
    sys.exit(1)

textFile = sys.argv[1]
outputFile = sys.argv[2]

# Check if the input file exists
if os.path.exists(textFile):
    # 'r' mode used, file open to read
    with open(textFile, 'r') as file:
        # reading the file
        file_words = file.read()

    words = re.findall(r'\b\w+\b', file_words.lower())
    word_count = {}
    for word in words:
        # filling dictionary and counting words
        word_count[word] = word_count.get(word, 0) + 1

    sorted_word_count = dict(sorted(word_count.items()))

    # file open to appending and writing
    with open(outputFile, 'a+') as out:
        for word, count in sorted_word_count.items():
            out.write(f"{word} {count}\n")
else:
    print("Sorry, the input file does not exist or the path is incorrect.")