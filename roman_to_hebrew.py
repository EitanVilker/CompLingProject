### Author: Kai Frey & Eitan Vilker
### Iterate through the Hebrew & translated parallel corpus to get the rules for transliteration
### Should be 1:1 other than the final forms. Final forms denoted by *_

import csv

transliteration = {} 
final_chars = ['c', 'k', 'm', 'n', 'p']

with open("hebrewToTransliterated.csv", 'r') as corpus:
  reader = csv.reader(corpus)
  line_count = 0
  for row in reader:
    if line_count != 0:
      heb = row[1].split()
      rom = row[2].split()
      if len(rom) == len(heb):
        for i in range(len(rom)):
          heb_word = heb[i]
          rom_word = rom[i]
          # look at each char in word
          for i in range(len(rom_word)):
            char = rom_word[i]
            heb_char = heb_word[i]
            if char.isnumeric() or char == '"':
              continue
            # special case for final forms
            # if end of the word, make input as n_, p_, k_, c_, m_. Else n, p, k, c, m
            if char in final_chars and i == len(rom_word)-1:
              char = rom_word[i] + '_'

            if char not in transliteration.keys():  
              transliteration[char] = {heb_char : 1}
            else:
              if heb_char in transliteration[char].keys():
                transliteration[char][heb_char] += 1
              else:
                transliteration[char][heb_char] = 1
    else: line_count +=1

# clean up transliteration

for key in transliteration:
  to_remove = []
  for nested_key in transliteration[key]:
    if transliteration[key][nested_key] == 1:
      to_remove.append(nested_key)
  for item in to_remove:
    transliteration[key].pop(item)
# remove the non-final forms from final pe & mem
transliteration['p_'].pop('פ')
transliteration['m_'].pop('מ')


print(transliteration)
          