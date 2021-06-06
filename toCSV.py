### Author: Kai Frey & Eitan Vilker
### Converts the raw text files from https://yeda.cs.technion.ac.il/resources_treebank.html 
### into a csv to use as training data. 
### Sections off phrases based on punctuation & new lines

### Appends the data from the hebrewToTransliteration to the end of the csv. This is from 
### https://yeda.cs.technion.ac.il/resources_lexicons_mila.html

import csv
import re

# files to convert into csv
def rom_heb_csv():
  hebrew = open('hebrewRaw.txt', 'r')
  romanized = open('transliteratedRaw.txt', 'r')
  csv_id = 0

  with open('hebrewToTransliterated.csv', mode="w") as csv_file:
    file_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # write the fields
    file_writer.writerow(['id', 'hebrew', 'transliterated'])
    h_curr = ""
    r_curr = ""
    # read from each line
    for h_line, r_line in zip(hebrew, romanized):
      # get the words
      h_words = h_line.split()
      r_words = r_line.split()
      # current phrases
      h_curr = ""
      r_curr = ""
      for i in range(len(h_words)-1):
        # check that it is a useful item
        # if it is a word, not punctuation, add to current phrase
        if h_words[i].isalnum() and r_words[i].isalnum():
          # remove letters
          h_curr = re.sub('[0-9]*', '', h_curr)
          r_curr = re.sub('[0-9]*', '', r_curr)
          h_curr += (h_words[i] + " ") # add right to left
          r_curr += (r_words[i] + " ")
        # otherwise, clean up the current phrase & write to the csv
        elif h_curr != "" and r_curr != "":
          file_writer.writerow([csv_id, h_curr.strip(), r_curr.strip()])
          h_curr = ""
          r_curr = ""
          csv_id += 1   # increase the id by one
      # if at the end of line, add curr phrases
      if h_curr != "" and r_curr != "":
        file_writer.writerow([csv_id, h_curr.strip(), r_curr.strip()])
        csv_id += 1
        

    # Append the information from hebrewToTransliteration
    with open('hebrew_translit_raw.csv', 'r') as lexicon:
      lex_reader = csv.reader(lexicon, delimiter=',')
      # get each row
      header = 0 # acting as a true/false
      for row in lex_reader:
        if header == 0:
          header = 1 # have made it past the header!
          continue # get out of this iteration
        # otherwise, add our id, the hebrew, & the transliteration
        # replace Arabic/punctuation with null
        h_curr = re.sub('[\'؂U]+', '', row[1])
        r_curr = re.sub(r"null", '', row[2])
        if h_curr != '' and r_curr != '':
          file_writer.writerow([csv_id, h_curr.strip(), r_curr.strip()])
          csv_id += 1

  hebrew.close()
  romanized.close()
  


# the NMT is unable to read the heb.txt file, which is tab delimited.
# This is because the tabs & the RTL language are not working well together
# So we remove all commas in the phrases and turn it into a csv
# I went and made sure all lines were correctly formatted: If run again, alter the first 2 lines. 
def heb_eng_csv():
  with open('heb_eng.csv', 'w') as heb_csv:
    with open('heb.txt', 'r') as heb:
      # can't use " as quotechar bc it is used in the heb.txt. | not in file
      writer = csv.writer(heb_csv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      # read through each line
      for line in heb:
        split_line = line.split("\t")
        eng = split_line[0]
        eng = re.sub(',*', '', eng)
        heb = split_line[1]
        heb = re.sub(',*', '', heb)
        writer.writerow([eng, heb])



heb_eng_csv()