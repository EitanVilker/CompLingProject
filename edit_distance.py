# Authors: Eitan Vilker and Kai Frey (eitan.e.vilker.21@dartmouth.edu and kai.m.frey.22@dartmouth.edu)
# Usage: Simply run with python edit_distance and enter input when prompted

# Function to create a list of tuples of words and frequencies based on a corpus
# Said list is sorted in descending order by the frequencies
def createOrderedWordFrequencyList(file):

    freqList = []

    file = open(file, "r")
    for line in file:
        freqList.append([line[0], line[1]])
    
    freqList = sorted(freqList, key=itemgetter(1))
    file.close()

    return freqList

# Function to get the closest word based on its frequency and its edit distance
def getClosestWord(word, freqList):

    currentBestWord = ""
    currentBestDistance = 9999
    editDistance = 0
    
    for i in range(len(freqList)):
        editDistance = damerauLevenshtein(word,freqList[i][0])
        if editDistance < currentBestDistance:
            currentBestDistance = editDistance
            currentBestWord = word
            if currentBestDistance == 0:
                break
    
    return currentBestWord


freqList = createOrderedWordFrequencyList("dummy_file.txt")
while(True):
    word = input("Enter your Hebrew word: ")
    print("\nYou entered: " + word)
    print("This was converted to: " + getClosestWord(word, freqList))