import csv

# files to convert into csv
hebrew = open('hebrewRaw.txt', 'r')
romanized = open('transliteratedRaw.txt', 'r')
csv_id = 0

with open('rawToCSV.csv', mode="w") as csv_file:
  file_writer = csv.writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
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


hebrew.close()
romanized.close()