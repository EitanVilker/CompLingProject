# Authors: Eitan Vilker and Kai Frey (eitan.e.vilker.21@dartmouth.edu and kai.m.frey.22@dartmouth.edu)
# Usage: Simply run with python edit_distance and enter input when prompted

from fastDamerauLevenshtein import *

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
def getClosestWord(word, freqList):

    currentBestWord = ""
    currentBestDistance = 9999
    editDistance = 0
    
    for i in range(len(freqList)):
        current = freqList[i][0]
        editDistance = damerauLevenshtein(word,current, False)
        if editDistance < currentBestDistance:
            currentBestDistance = editDistance
            currentBestWord = current
            if currentBestDistance == 0:
                break
            
    return currentBestWord


# freqList = createOrderedWordFrequencyList("dummy_file.txt")
# while(True):
#     word = input("Enter your Hebrew word: ")
#     print("\nYou entered: " + word)
#     print("This was converted to: " + getClosestWord(word, freqList))