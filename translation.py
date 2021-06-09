### Author: Kai Frey & Eitan Vilker
### Create a dictionary of Hebrew words to their possible English definitions
### Uses data from heb_eng.csv
import csv
import re

# Special cases, manually input to dictionary. Increasing this would make this a better translation dictionary
common_words = {'שלנו': 'our', 'אנחנו': 'we', 'היא': 'she', 'אותי': 'me', 'זה': 'it', 'ו': 'and',
        'אתה': 'you', 'אותך': 'you', 'שלך': 'your', 'הוא': 'he', 'אל': 'to', 'שלי': 'my', 'היה': 'was', 'ב': 'in',
        'אני': 'i', 'איך': 'how', 'הם': 'they', 'הן': 'they', 'ל': 'of',
        'את': 'et, which has no translation but denotes a direct object'}
names = ['john', 'mary', 'tom', "tom's", "mary's", "john's"]
issue_words = ['the', 'a', 'an', "i'm", "how's", 'are', "i'll", 'be', 'is']
phrase_dictionary = {}
dictionary = {}

## generate a dictionary of all hebrew words & phrases with them in it
with open('heb_eng.csv', 'r') as heb_eng:
    reader = csv.reader(heb_eng)
    for row in reader:
        # split and clean into words
        eng = row[0].strip('.,?!"')
        heb = row[1].strip('.,?!"').split()
        phrase = re.sub('",', '', eng)
        for word in heb:
            word = re.sub(r'[",]*', '', word)
            if word in phrase_dictionary.keys():
                phrase_dictionary[word].append(phrase)
            else:
                # a list of phrases
                phrase_dictionary[word] = [phrase]

# get words associated with each individual Hebrew word
for key, phrases in phrase_dictionary.items():
    if key in common_words:
        continue
    words_freq = {}
    possible_translations = []
    all_words = []
    for phrase in phrases:
        english = phrase.lower().split()
        all_words.extend(english)
    for word in all_words:
        # ignore some words
        word = word.strip()
        if word in names or word in issue_words or word in common_words.values():
            continue
        if word in words_freq:
            words_freq[word] += 1
        else: 
            words_freq[word] = 1
    # add highest 3 words, if there is more than 2 options, should show up at least 10 times
    for word in sorted(words_freq, key=words_freq.get, reverse=True):
        if len(possible_translations) == 2:
            if words_freq[word] >= 10:
                possible_translations.append(word)
        if len(possible_translations) < 2:
            possible_translations.append(word)
    dictionary[key] = possible_translations

## Input: a Hebrew word in Hebrew characters
## Output: an list of English words that it could mean
def translate(hebrew):
    word = hebrew
    if word in common_words:
        return([common_words[word]])
    elif word not in dictionary or dictionary[word] == []:
        return(["we are unable to translate this word"])
    else: return dictionary[word]