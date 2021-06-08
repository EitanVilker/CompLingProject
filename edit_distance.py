# Authors: Eitan Vilker and Kai Frey (eitan.e.vilker.21@dartmouth.edu and kai.m.frey.22@dartmouth.edu)
# Usage: pip install fastDamerauLevenshtein
# Simply run with python edit_distance and enter input when prompted

# Geeks For Geeks edit distance code used as inspiration
# https://www.geeksforgeeks.org/edit-distance-dp-5/

from fastDamerauLevenshtein import damerauLevenshtein
import sys

def createDoubleLetterLookup():

    lookup = {}
    lookup["כ"] = ["ק","ח"]
    lookup["ק"] = ["כ"]
    lookup["א"] = ["ע"]
    lookup["ע"] = ["א"]
    lookup["ש"] = ["ס"]
    lookup["ס"] = ["ש"]
    lookup["ת"] = ["ט"]
    lookup["ט"] = ["ת"]
    lookup["ו"] = ["ב"]
    lookup["ב"] = ["ו"]
    lookup["ג"] = ["NDL"]
    lookup["ד"] = ["NDL"]
    lookup["ה"] = ["NDL"]
    lookup["ז"] = ["NDL"]
    lookup["ח"] = ["ך‎‎", "כ"]
    lookup["י"] = ["NDL"]
    lookup["ל"] = ["NDL"]
    lookup["מ"] = ["NDL"]
    lookup["נ"] = ["NDL"]
    lookup["ן"] = ["NDL"]
    lookup["פ"] = ["NDL"]
    lookup["ף"] = ["NDL"]
    lookup["צ"] = ["NDL"]
    lookup["ר"] = ["NDL"]
    lookup["ץ"] = ["NDL"]
    lookup["ם‎"] = ["NDL"]
    lookup["ך‎‎"] = ["כ"]
    
    return lookup

def createEmptyDynamicTable(length1, length2):
    dp = [[-1 for i in range(length2 + 1)] for j in range(length1 + 1)]
    return dp

def customEditDistance(word1, word2, length1, length2, editDistanceTable, lookup):

    if length1 == 0:
        return length2
    if length2 == 0:
        return length1

    if editDistanceTable[length1][length2] != -1:
        return editDistanceTable[length1][length2]

    # If letters are equal
    if word1[length1 - 1] == word2[length2 - 1]:
        if editDistanceTable[length1 - 1][length2 - 1] == -1:
            editDistanceTable[length1][length2] = customEditDistance(word1, word2, length1 - 1, length2 - 1, editDistanceTable, lookup)
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
        costDeletion = customEditDistance(word1, word2, length1 - 1, length2, editDistanceTable, lookup)

    # Insertion
    if editDistanceTable[length1][length2 - 1] != -1:
        costInsertion = editDistanceTable[length1][length2 - 1]
    else:
        costInsertion = customEditDistance(word1, word2, length1, length2 - 1, editDistanceTable, lookup)

    # Replacement
    possibleDoubles = lookup[word1[length1 - 1]]
    if editDistanceTable[length1 - 1][length2 - 1] != -1:
        costReplacement = editDistanceTable[length1 - 1][length2 - 1]
        for i in possibleDoubles:
            if word1[length2 - 1] == i:
                costReplacement -= .75
    else:
        costReplacement = customEditDistance(word1, word2, length1 - 1, length2 - 1, editDistanceTable, lookup)
        for i in possibleDoubles:
            if word1[length1 - 1] == i:
                costReplacement -= .75

    editDistanceTable[length1][length2] = 1 + min(costDeletion, min(costInsertion, costReplacement))
    
    return editDistanceTable[length1][length2]


# Function to get the closest word based on its frequency and its edit distance
def getClosestWords(word, freqList, usingCustomEditDistance):

    currentBestDistance = sys.maxsize
    lastWordDistance = sys.maxsize
    wordsList = []
    editDistance = 0
    lookup = createDoubleLetterLookup()
    
    for i in range(len(freqList)):

        current = freqList[i][0]

        if usingCustomEditDistance:
            editDistanceTable = createEmptyDynamicTable(len(word), len(current))
            editDistance = customEditDistance(word, current, len(word)-1, len(current)-1, editDistanceTable, lookup)
        else:
            editDistance = damerauLevenshtein(word,current, similarity=False)

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

# Driver code

str1 = "כלכככ"
str2 = "קלכככ"

lookup = createDoubleLetterLookup()
dp = createEmptyDynamicTable(len(str1), len(str2))

print(customEditDistance(str1, str2, len(str1), len(str2), dp, lookup))