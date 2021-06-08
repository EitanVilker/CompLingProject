#!/usr/bin/env python
# -*- coding: utf-8 -*-

import transliteration
import edit_distance
import roman_to_hebrew
import translation
# import tensorflow as tf
# from tensorflow.keras.layers.experimental import preprocessing

# import tensorflow_text as tf_text

# print(tf.__version__)

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
        heb_word = roman_to_hebrew.letter_dict[l] + heb_word
    return heb_word

def run(rom_word, customEditDistance):
    print("\nYou entered: " + rom_word)
    word = transliterate_word(rom_word)
    print(word)
    wordsList = edit_distance.getClosestWords(word, freqList, customEditDistance)
    print("The best word is " + wordsList[0][0] + " with edit distance " + str(wordsList[0][1])) 
    print("This could mean: " + write_translations(wordsList[0][0]))
    print("Other possibilities include: ")
    for i in range(len(wordsList)-1):
        print(wordsList[i + 1][0] + " which could mean: " + write_translations(wordsList[i+1][0]))
    return wordsList[0][0]

def write_translations(word):
    string = ""
    words = translation.translate(str(word))
    for i in range(len(words)):
        string += words[i]
        if i != len(words)-1:
            string += ' or '
    return string

def collectAccuracies(outputFile, usingCustomEditDistance):
    
    print("Enter q to quit")
    file = open(outputFile, "a") # Important to append rather than overwrite
    while(True):
        word = input("Enter your Hebrew word: ")
        if word == "q":
            file.close()
            break
        run(word, usingCustomEditDistance)
        wasTheFirstWordRight = input("Enter 1 if the first word provided was right, and 0 otherwise: ")
        if wasTheFirstWordRight == "q":
            file.close()
            break
        wasTheWordInList = input("Enter 1 if the word was in the list (including the first word) and 0 otherwise: ")
        if wasTheWordInList == "q":
            file.close()
            break
        file.write(word + "," + wasTheFirstWordRight + "," + wasTheWordInList + "\n")

def automaticallyCollectAccuracies(inputFile, usingCustomEditDistance):

    correct = 0
    incorrect = 0

    file = open(inputFile, "r", encoding="utf8")
    for line in file:
        line = line.split(",")
        word = run(line[0], usingCustomEditDistance)
        print(line[1])
        if word == line[1]:
            correct  += 1
        else:
            incorrect += 1
    return correct / (correct + incorrect)

def runNormal(customEditDistance):
    while(True):
        word = input("Enter your Hebrew word: ")
        run(word, customEditDistance)

freqList = createOrderedWordFrequencyList("occurrences.csv")
lookup = edit_distance.createDoubleLetterLookup()
usingCustomEditDistance = False

# collectAccuracies("outputFile.csv", usingCustomEditDistance)
# print(automaticallyCollectAccuracies("testing.csv", usingCustomEditDistance))
runNormal(usingCustomEditDistance)