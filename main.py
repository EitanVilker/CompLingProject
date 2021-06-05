#!/usr/bin/env python
# -*- coding: utf-8 -*-

import transliteration
import edit_distance

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

freqList = createOrderedWordFrequencyList("occurrences.csv")

while(True):
    word = input("Enter your Hebrew word: ")
    print("\nYou entered: " + word)
    wordsList = edit_distance.getClosestWords(word.strip(), freqList)
    print("The best word is " + wordsList[0][0] + ", which means " + hebrewToEnglish(wordsList[0][0]))
    print("Other possibilities include: ")
    
    for i in range(9):
        print(wordsList[i + 1] + translation.hebrewToEnglish(wordsList[i + 1][0]))