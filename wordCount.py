#! /usr/bin/env python3.12

import os
import re

input = "C:\\Users\\Diana\\Desktop\\2024 spring\\os\\python-intro-dianaOli\\input.txt"
output = "C:\\Users\\Diana\\Desktop\\2024 spring\os\\python-intro-dianaOli\\output.txt"

#check if file exist
if os.path.exists(input):
    # 'r' mode used, file open to read
    with open(input, 'r') as file:
        #reading the file 
        file_words = file.read()
        #writing bytes to file descriptor, encode() converting string to bytes
        #fancy print 
        #os.write(1,file_words.encode())
    words = re.findall(r'\b\w+\b', file_words.lower())
    #add words to a list
    #words_list = file_words.split()
    #dictionary
    word_count = {}
    for word in words:
       
        
        #filling dictionary and counting words 
        word_count[word] = word_count.get(word,0)+1

    sorted_word_count = dict(sorted(word_count.items()))
    #file open to appending and writing
    with open(output, 'a+') as out:

        for word, count in sorted_word_count.items():
            out.write(f"{word}: {count}\n")

    
else:
    print("sorry i didn't find a text file,check path")