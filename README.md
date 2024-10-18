# Dzongkha Spell Checker
This project is about a Dzongkha spell checker for the Dzongkha words. It Compares word by word from an input txt file with the dictionary txt file and gives the incorrect words and identify the misspelled words. This program is made in Python and uses a set-based approach for efficient dictionary lookups.

# Table of Contents
Usage
Implementation Details
Data Structures
Algorithms
Challenges and Solutions
Future Improvements
References

# Usage
To use this spellchecker, we need to run the following command:

--python dzongkha_spell_checker.py input_file.txt--

Where the input_file.txt is the name of the file containing the text that needs to be checked.

Before doing so we must have : Python 3.x, requests, and docx2txt downloaded

# Implementation Details
First we downloaded the input txt file using the 'requests' library and then we useed the 'docx2txt' library to convert the dictionary docx file into txt file. After that we cleaned the dictionary txt file, removing all unwanted characters and english letters from the dictionary.
Then we identify all the incorrect words in the input txt file by comparing the cleaned dictionary file and the input txt and we display the incorrect words with their line numbers and word positions to the user.

# Data Structures
The main data structure used:
1. words_ (dictionary): Stores words from input txt file, along with line and word positions. We used it to track the context of misspelled words.
2. dictionary_words (set): Stores words from dictionary, allowing comparison against words from input txt file and dictionary
3. incorrect_words (dictionary): Stores the incorrect words found in the input txt file, along with their line and their positions.

# Algorithms
File Conversion:
Converts a DOCX dictionary file to a TXT file using the docx2txt library.

File Download:
Downloaded the text file containing the incorrect Dzongkha words from the URL using the requests library.

Data Cleaning:
Read the dictionary file, remove all unwanted texts and character like '་','།' and clean the txt file, and save them to a cleaned txt file.

Spell Checking:
Reads the input text file and the cleaned dictionary file, and compares this two files to find the incorrect word, and records the line numbers and positions of incorrect words.

# Perfromance Analysis
The provided code is functional and efficient for the dzo spelling checker use but may require optimization for handling larger files or datasets.

# Challenges and Solutions
One of the main challenges I encountered was the lack of readily available Dzongkha dictionary words. which was solved by manually creating a dictionary of Dzongkha words.
Another challenge was the handling the Dzongkha characters like '་' and '།'. It was solved by making the '་' as the standarded space and spilt the lines with it.

# Future Improvements
In the future, improve the spelling checker by adding features such as:
Support for Dzongkha phonetic spelling
A more robust cleaning algorithm
Support for multiple dictionaries
A user interface for easier interaction

# References
# 1.blackbox.ai (https://www.blackbox.ai/chat/expert-python)
# 2.w3school (https://www.w3schools.com/)
# 3.Chatgpt (https://chatgpt.com/)
# 4.youtube (https://www.youtube.com/)