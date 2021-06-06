# Authors: Eitan Vilker and Kai Frey (eitan.e.vilker.21@dartmouth.edu and kai.m.frey.22@dartmouth.edu)
# Usage: pip install fastDamerauLevenshtein
# Simply run with python edit_distance and enter input when prompted

# Geeks For Geeks edit distance code used as inspiration
# https://www.geeksforgeeks.org/edit-distance-dp-5/

from fastDamerauLevenshtein import damerauLevenshtein
import sys

def customEditDistance(word1, word2, length1, length2, editDistanceTable):

    if length1 == 0:
        return length2
    if length2 == 0:
        return length1

    if editDistanceTable[n][m] != -1:
        return editDistanceTable[n][m]
    
    # If letters are equal
    if word1[length1 - 1] == word2[length2 - 1]:
        if editDistanceTable[length1 - 1][length2 - 1] == -1:
            editDistanceTable[length1][length2] = customEditDistance(word1, word2, length1 - 1, length2 - 1, editDistanceTable)
            return editDistanceTable[length1][length2]
        
        editDistanceTable[length1][length2] = editDistanceTable[length1 - 1][length2 - 1]
        return editDistanceTable[length1][length2]
    
    # If letters aren't equal, find cost of insertion, deletion, and replacement
    
    costInsertion = 0
    costDeletion = 0
    costReplacement = 0

    # Deletion
    if editDistanceTable[length1 - 1][length2] != -1:
        costDeletion = editDistanceTable[length1 - 1][length2]
    else:
        costDeletion = customEditDistance(word1, word2, length1 - 1, length2, editDistanceTable)

    # Insertion
    if editDistanceTable[length1][length2 - 1] != -1:
        costInsertion = editDistanceTable[length1][length2 - 1]
    else:
        costInsertion = customEditDistance(word1, word2, length1, length2 - 1, editDistanceTable)

    # Replacement
    if editDistanceTable[length1 - 1][length2 - 1] != -1:
        costReplacement = editDistanceTable[length1 - 1][length2 - 1]
    else:
        costReplacement = customEditDistance(word1, word2, length1 - 1, length2 - 1, editDistanceTable)

    editDistanceTable[length1][length2] = 1 + min(costDeletion, min(costInsertion, costReplacement))
    
    return editDistanceTable[length1][length2]

# # Function to create a list of tuples of words and frequencies based on a corpus
# # Said list is sorted in descending order by the frequencies
# def createOrderedWordFrequencyList(file):
#     freqList = []
#     file = open(file, "r")
#     for line in file:
#         line = line.split()
#         freqList.append([line[0], line[1]])
    
#     freqList = sorted(freqList, key=lambda item: (item[1]), reverse=True)
#     print(freqList)
#     file.close()

#     return freqList

# Function to get the closest word based on its frequency and its edit distance
def getClosestWords(word, freqList):

    currentBestDistance = sys.maxsize
    lastWordDistance = sys.maxsize
    wordsList = []
    editDistance = 0
    
    for i in range(len(freqList)):
        current = freqList[i][0]
        editDistance = damerauLevenshtein(word,current, similarity=False)

        if editDistance < 5:
            print(word,current)
        
        # Check if word is the best one and should go at front of list
        if editDistance < currentBestDistance:
            currentBestDistance = editDistance
            wordsList.insert(0, [current, editDistance])
            if len(wordsList) > 10:
                wordsList.pop(10)
        
        # Put word in appropriate place in list if not best word
        elif editDistance < lastWordDistance:
            for i in range(len(wordsList)):
                if wordsList[i][1] > editDistance:
                    wordsList.insert(i, [current, editDistance])
                    if len(wordsList) > 10:
                        wordsList.pop(10)
        
        # If list has less than ten entries, add word to appropriate spot in list
        elif len(wordsList) < 10:
            wordInserted = False
            for i in range(len(wordsList)):
                if wordsList[i][1] > editDistance:
                    wordsList.insert(i, [current, editDistance])
                    wordInserted = True
                    break
            if wordInserted == False:
                wordsList.append([current, editDistance])
                lastWordDistance = editDistance
            
    return wordsList

print(damerauLevenshtein("Hello", "Hello", similarity=False))

# freqList = createOrderedWordFrequencyList("dummy_file.txt")
# while(True):
#     word = input("Enter your Hebrew word: ")
#     print("\nYou entered: " + word)
#     print("This was converted to: " + getClosestWord(word, freqList))