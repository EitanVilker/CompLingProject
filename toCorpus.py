### Author: Kai Frey
### Coverts the raw text from https://github.com/ajinkyakulkarni14/TED-Multilingual-Parallel-Corpus/blob/master/Monolingual_data/Hebrew.txt
### into a corpus with each word and the number of times it appears in the text

import csv
import string
import re

word_dict = {}
w_id = 0
# generate the dictionary first, then write to the csv
with open('ted_hebrew.txt', 'r') as txt_file:
  # run through every word
  for line in txt_file:
    # split and remove punctuation
    words = line.split()
    for w in words:
      # remove all but hebrew letters
      w = re.sub('[^\u05D0-\u05EA]+', '', w)
      if w == '':
        continue
      if w not in word_dict.keys():
        word_dict[w] = 1
      else:
        word_dict[w] += 1
  # write csv
  with open('occurrences.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['id', 'freq', 'word'])

    for word, freq in word_dict.items():
      writer.writerow([w_id, freq, word.strip()])
      w_id += 1