### Author: Kai Frey & Eitan Vilker
### Create a dictionary of Hebrew words to their possible English definitions
### Uses data from heb_eng.csv
import csv
import re

dictionary = {}

## generate a dictionary of all hebrew words & phrases with them in it
with open('heb_eng.csv', 'r') as heb_eng:
    reader = csv.reader(heb_eng)
    for row in reader:
        # split and clean into words
        eng = row[0].strip('.,?!"')
        heb = row[1].strip('.,?!"').split()
        phrase = re.sub('",', eng)
        for word in heb:
            word = re.sub('",', word)
            if word in dictionary.keys:
                dictionary[word].append(phrase)
            else:
                # a list of phrases
                dictionary[word] = [phrase]
            
        

## Input: a Hebrew word in Hebrew characters
## Output: an English word or list of words that could be 
def translate(hebrew):
    return('english')