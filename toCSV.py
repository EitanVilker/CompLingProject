### Author: Kai Frey
### Converts the raw text files from https://yeda.cs.technion.ac.il/resources_treebank.html 
### into a csv to use as training data

### Appends the data from the hebrewToTransliteration to the end of the csv. This is from 
### https://yeda.cs.technion.ac.il/resources_lexicons_mila.html

import csv

# files to convert into csv
hebrew = open('hebrewRaw.txt', 'r')
romanized = open('transliteratedRaw.txt', 'r')
csv_id = 0

with open('rawToCSV.csv', mode="w") as csv_file:
  file_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  # write the fields
  file_writer.writerow(['id', 'hebrew', 'transliterated'])
  # read one word from each file
  for h_line, r_line in zip(hebrew, romanized):
    # get the words
    h_words = h_line.split()
    r_words = r_line.split()
    for i in range(len(h_words)-1):
      # check that it is a useful item
      rtl_i = len(h_words)-1-i # get the right to left word at location i
      if h_words[rtl_i].isalnum() and r_words[i].isalnum():
        # same order as the other csv: id, hebrew, transliterated
        file_writer.writerow([csv_id, h_words[i], r_words[i]])
        csv_id += 1   # increase the id by one

  # Append the information from hebrewToTransliteration
  with open('hebrewToTransliterated.csv', 'r') as lexicon:
    lex_reader = csv.reader(lexicon, delimiter=',')
    # get each row
    header = 0 # acting as a true/false
    for row in lex_reader:
      if header == 0:
        header = 1 # have made it past the header!
        continue # get out of this iteration
      # otherwise, add our id, the hebrew, & the transliteration
      file_writer.writerow([csv_id, row[1], row[2]])
      csv_id += 1

hebrew.close()
romanized.close()
  