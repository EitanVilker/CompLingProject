
import transliteration.py
import edit_distance.py

# Function to create a list of tuples of words and frequencies based on a corpus
# Said list is sorted in descending order by the frequencies
def createOrderedWordFrequencyList(file):
    freqList = []
    file = open(file, "r")
    for line in file:
        line = line.split()
        freqList.append([line[0], line[1]])
    
    freqList = sorted(freqList, key=lambda item: (item[1]), reverse=True)
    print(freqList)
    file.close()

def createWordMeaningDict(file):
    file = file.open()
    wordMeaningDict = {}
    for line in file:
        line = line.split(",")
        freqDict[line[1]] = line[2]

freqList = createOrderedWordFrequencyList("occurences.csv")
while(True):
    word = input("Enter your Hebrew word: ")
    print("\nYou entered: " + word)
    print("This was converted to: " + edit_distance.getClosestWord(word, freqList))
    
    #if (translating):
    #    print("This means: " + )