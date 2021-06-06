# English to Hebrew Transliteration

### How to Run

If you download this whole project, you can simply run ./main.py or python main.py. You will then be prompted to enter Hebrew words in English letters.

### Idea

The goal of our project is simple- we want to be able to sound out a word in English letters and get back a Hebrew word and definition. For instance, if you type "sifriyah," you would get a list of possible spellings along with definitions, with ideally "ספריה" being the first result.

The flowchart looks like this:
1. User enters Hebrew word sounded out with English characters; for instance, "sifriyah"
2. The word is converted to machine-understandable Romanized Hebrew using a rule-based logical system; for instance, "efrih"
3. The word is converted to actual Hebrew characters using a simple one-to-one conversion of Romanized Hebrew letters to Hebrew letters; for instance, "ספריה"
4. The word is spell-checked using Damerau-Levenshtein edit distance and frequency analysis to find the most likely matches; in this case, the word is exactly the one desired, so it will simply be "ספריה" again
5. The list of words is translated back into English; for instance, the first member of the list would be \["ספריה", "library"]
6. The list of words is outputted to the user


