#!/usr/bin/env python
# -*- coding: utf-8 -*-

import transliteration
import edit_distance
import roman_to_hebrew

# Function to create a list of tuples of words and frequencies based on a corpus
# Said list is sorted in descending order by the frequencies
def createOrderedWordFrequencyList(file):
    freqList = []
    file = open(file, "r", encoding='utf8')
    for line in file:
        line = line.split(",")
        if int(line[1]) != 1: # only add if it occurs more than once
            freqList.append([line[2].strip('\n'), int(line[1])])


    freqList = sorted(freqList, key=lambda item: (item[1]), reverse=True)
    file.close()
    return freqList

def createWordMeaningDict(file):
    file = file.open()
    freqDict = {}
    for line in file:
        line = line.split(",")
        freqDict[line[1]] = line[2]

def transliterate_word(word):
    mt_word = transliteration.convertToMachineTransliteration(word)
    heb_word = ""
    for i in range(len(mt_word)):
        l = mt_word[i]
        if l in roman_to_hebrew.final_chars and i == len(mt_word)-1:
            l += '_'
        heb_word += roman_to_hebrew.letter_dict[l]
    return heb_word

def run(rom_word):
    print("\nYou entered: " + rom_word)
    word = transliterate_word(rom_word)
    wordsList = edit_distance.getClosestWords(word.strip(), freqList)
    print("The best word is " + wordsList[0][0] )
    # + ", which means " + hebrewToEnglish(wordsList[0][0]))
    print("Other possibilities include: ")
    for i in range(len(wordsList)-1):
        print(wordsList[i + 1] )
        # + translation.hebrewToEnglish(wordsList[i + 1][0]))

def collectAccuracies(outputFile):
    
    file = open(outputFile, "a") # Important to append rather than overwrite
    while(True):
        word = input("Enter your Hebrew word: ")
        run(word)
        wasTheFirstWordRight = input("Enter 1 if the first word provided was right, and 0 otherwise: ")
        wasTheWordInList = input("Enter 1 if the word was in the list (including the first word) and 0 otherwise: ")
        file.write(word + "," + wasTheFirstWordRight + "," + wasTheWordInList)

def runNormal():
    while(True):
        word = input("Enter your Hebrew word: ")
        run(word)

freqList = createOrderedWordFrequencyList("occurrences.csv")

# runNormal()

collectAccuracies("outputFile.csv")