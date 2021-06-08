### Author: Kai Frey & Eitan Vilker
### Collection of all functions that convert data to CSVs for use

import csv
import re

## Converts the raw text files from https://yeda.cs.technion.ac.il/resources_treebank.html 
## into a csv for use to generate transliteration rules.
## Sections off phrases based on punctuation & new lines

## Appends the data from the hebrewToTransliteration to the end of the csv. This is from 
## https://yeda.cs.technion.ac.il/resources_lexicons_mila.html

def rom_heb_csv():
  hebrew = open('text_data/hebrewRaw.txt', 'r')
  romanized = open('text_data/transliteratedRaw.txt', 'r')
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
    with open('text_data/hebrew_translit_raw.csv', 'r') as lexicon:
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
  
## Coverts the raw text from 
## https://github.com/ajinkyakulkarni14/TED-Multilingual-Parallel-Corpus/blob/master/Monolingual_data/Hebrew.txt
## into a corpus with each word and the number of times it appears in the text
## Used for edit distance
def occurances_csv():
  word_dict = {}
  w_id = 0
  # generate the dictionary first
  with open('text_data/ted_hebrew.txt', 'r') as txt_file:
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

## the NMT is unable to read the heb.txt file, which is tab delimited.
## This is because the tabs & the RTL language are not working well together
## So we remove all commas in the phrases and turn it into a csv
## I went and made sure all lines were correctly formatted: If run again, alter the first 2 lines. 

## Though NMT is no longer is part of the project, this CSV is still helpful for creating the dictionary
def heb_eng_csv():
  with open('heb_eng.csv', 'w') as heb_csv:
    with open('text_data/heb.txt', 'r') as heb:
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

# rom_heb_csv()
# occurances_csv()
# heb_eng_csv()