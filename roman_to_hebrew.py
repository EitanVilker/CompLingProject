## Author: Kai Frey & Eitan Vilker
## Iterate through the Hebrew & translated parallel corpus to get the rules for transliteration
import csv

transliteration = {} 

with open("hebrewToTransliterated.csv", 'r') as corpus:
