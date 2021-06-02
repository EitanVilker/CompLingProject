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
        freqList.append([line[2], line[1]])

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
    print("Printing shel: ")
    print("של")
    word = input("Enter your Hebrew word: ")
    print("\nYou entered: " + word)
    print("This was converted to: " + edit_distance.getClosestWord(word, freqList))
    
    #if (translating):
    #    print("This means: " + )