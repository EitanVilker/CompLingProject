# Authors: Eitan Vilker and Kai Frey (eitan.e.vilker.21@dartmouth.edu and kai.m.frey.22@dartmouth.edu)
# Usage: pip install fastDamerauLevenshtein
# Simply run with python edit_distance and enter input when prompted

from fastDamerauLevenshtein import damerauLevenshtein
import sys

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
        
        # Check if word is the best one and should go at front of list
        if editDistance < currentBestDistance:
            currentBestDistance = editDistance
            wordsList.insert(0, [current, editDistance])
            if len(wordsList) > 10:
                wordsList.pop(10)
            if currentBestDistance == 0: # this is the same word, no need to look further
                break
        
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
            if wordInserted == False:
                wordsList.append([current, editDistance])
                lastWordDistance = editDistance
            
    return wordsList


# freqList = createOrderedWordFrequencyList("dummy_file.txt")
# while(True):
#     word = input("Enter your Hebrew word: ")
#     print("\nYou entered: " + word)
#     print("This was converted to: " + getClosestWord(word, freqList))