########################
# https://github.com/PemaLoselMaurer/SWE_CAPI_DZO_SPELL_CHECKER.git

#Pema Losel Maurer
#Swe 'A'
#02240353
#######################
# 1.blackbox.ai (https://www.blackbox.ai/chat/expert-python)
# 2.w3school (https://www.w3schools.com/)
# 3.Chatgpt (https://chatgpt.com/)
# 4.youtube (https://www.youtube.com/)

# Problem
# docx.txt can't be read
# inputfile is from online
# The dictionary has many unwanted characters
# Dzongkha words have different unicode code and gives wrong format
# white space when seperating the words 
# the word '་' cant act like white space and dilimiter
# everyword is compared, not the wanted words
# when giving positon, st nd rd nd are not assigned properly


#######################
# SOLUTION
#######################

# Read the input file
import requests

url = 'https://csf101-server-cap1.onrender.com/get/input/353'
txt_file = requests.get(url)

with open('353.txt', 'wb') as file:
    data = file.write(txt_file.content)

print('Download 353.txt')

# dco to txt
import docx2txt as d2t

Docfile="dictionary.docx"
txtfile="dictionary.txt"

doc=d2t.process(Docfile)

file=open(txtfile, 'w', encoding='utf-8')
file.write(doc)
file.close()

print("file converted")

# Clean the dictionary
def remove_dictionary(input, output):
    remove_words = []
    with open(input, 'r', encoding = "utf-8" )as file:
        for line in file:
            words = line.split()
            if words:
                dzongkha_words = words[0]
                remove_words.append(dzongkha_words)
    with open(output, "w", encoding = "utf-8") as file:
        for words in remove_words:
            file.write(words + "\n")
            print(f"remove words saved to {output}")
input = "dictionary.txt"
output = "removed.txt"
remove_dictionary(input, output)

# Main spelling checker
def read_words (txt_file):
    words_ = {}
    with open (txt_file, "r", encoding = "utf-8") as file:
        for line_number, line in enumerate (file, start = 1):
            words = line.split('་')
            for word_position, word in enumerate(words, start = 1):
                clean_word = word.strip().lower()
                if clean_word:  
                    words_[clean_word] = (line_number, word_position)
    return words_

def check_spelling (file_txt, dictionary_txt):
    text_words = read_words (file_txt)
    dictionary_words = read_words (dictionary_txt)

    incorrect_words = {word: text_words[word] for word in text_words if word not in dictionary_words}

    return incorrect_words

ordinal = lambda n:f"{n} {'th' 
                          if 10<= n % 100 <= 20
                            else {1:'st', 2:'nd', 3:'rd'}.get (n % 10, 'th') }"

text_file = '353.txt' 
dictionary_file = 'Cleaned.txt'

incorrect = check_spelling (text_file, dictionary_file)

print("The Incorrect spellig words:")
for word, (line, position) in incorrect.items():
        print(f"line: {line}, position: {ordinal(position)} word: {word}, is incorrect!!")


if __name__ == "__main__":
  import sys
  if len (sys.argv) != 2:
     print("Usage:python dzongkha_spell_checker.py<input_files>")
     sys.exit(1)

input_files = sys.argv[1]
dictionary_files = "dictionarys.txt"
check_spelling(input_files, dictionary_files)

