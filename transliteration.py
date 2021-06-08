# Authors: Eitan Vilker and Kai Frey (eitan.e.vilker.21@dartmouth.edu and kai.m.frey.22@dartmouth.edu)
# Usage: Simply run with python transliteration.py and enter Romanized Hebrew words when prompted

# Machine-transliterated Hebrew to Hebrew rules, for ease of reference
# a -> א
# b -> ב
# g -> ג
# d -> ד
# h -> ה
# w -> ו
# z -> ז
# x -> ח
# v -> ט
# i -> י
# k -> כ
# k (final) -> ך‎
# l -> ל
# m -> מ
# m (final) -> ם‎
# n -> נ
# n (final) -> ן
# s -> ס
# y -> ע 
# p -> פ
# p (final) -> ף
# c -> צ
# c (final) -> ץ
# q -> ק
# r -> ר
# e -> ש
# t -> ת


# Function that takes as input a word entered by a user and 
# outputs a word in the transliterated form computers can accept
def convertToMachineTransliteration(word):
    new_word = ""
    skip = False
    if_statment_fixer = True
    
    for i in range(len(word)):

        if word[i] == "s":
            if skip:
                skip = False
            elif i < len(word) - 1:
                if word[i + 1] == "h":
                    new_word += "e"
                    skip = True
                elif word[i + 1] == "s":
                    new_word += "s"
                    skip = True
                else:
                    new_word += "s"
            else:
                new_word += "s"
        
        elif word[i] == "c":
            if i < len(word) - 1:
                if word[i + 1] == "h":
                    new_word += "x"
                    skip = True
            else:
                new_word += "k"
        
        elif word[i] == "k":
            if i < len(word) - 1:
                if word[i + 1] == "h":
                    new_word += "x"
                    skip = True
                else:
                    new_word += "k"
            else:
                new_word += "k"

        elif word[i] == "h":
            if (skip):
                skip = False
            else:
                new_word += "h"
        
        elif word[i] == "b":
            if skip:
                skip = False
            elif i < len(word) - 1:
                if word[i + 1] == "b":
                    new_word += "b"
                    skip = True
                else:
                    new_word += "b"
            else:
                new_word += "b"
        
        elif word[i] == "g":
            new_word += "g"
        
        elif word[i] == "v":
            new_word += "w"
        
        elif word[i] == "z":
            if skip:
                skip = False
            else:
                new_word += "z"
        
        elif word[i] == "t":
            if skip:
                skip = False
            elif i < len(word) - 1:
                if word[i + 1] == "t":
                    new_word += "t"
                    skip = True
                elif word[i + 1] == "s" or word[i + 1] == "z":
                    new_word += "c"
                    skip = True
                else:
                    new_word += "t"
            else:
                new_word += "t"
        
        elif word[i] == "y":
            new_word += "i"
        
        elif word[i] == "l":
            if skip:
                skip = False
            elif i < len(word) - 1:
                if word[i + 1] == "l":
                    new_word += "l"
                    skip = True
                else:
                    new_word += "l"
            else:
               new_word += "l"
        
        elif word[i] == "m":
            if skip:
                skip = False
            elif i < len(word) - 1:
                if word[i + 1] == "m":
                    new_word += "m"
                    skip = True
                else:
                    new_word += "m"
            else:
                new_word += "m"
        
        elif word[i] == "n":
            if skip:
                skip = False
            elif i < len(word) - 1:
                if word[i + 1] == "n":
                    new_word += "n"
                    skip = True
                else:
                    new_word += "n"
            else:
                new_word += "n"

        elif word[i] == "p":
            new_word += "p"

        elif word[i] == "f":
            new_word += "p"
        
        elif word[i] == "r":
            new_word += "r"

        elif word[i] == "o":
            if skip:
                skip = False
            elif i < len(word) - 1:
                if word[i + 1] == "o":
                    new_word += "w"
                    skip = True
            else:
                new_word += "w"
        
        elif word[i] == "u":
            new_word += "w"
        
        elif word[i] == "i":
            if i == 0:
                new_word += "y"
            elif i == len(word) - 1:
                new_word += "i"
            elif word[i + 1] == "m":
                new_word += "im"
                skip = True
        
        elif word[i] == "a":
            if skip:
                skip = False
            elif i == 0:
                new_word += "a"
            elif i == len(word) - 1:
                new_word += "h"
            elif word[i + 1] == "a":
                new_word += "y"
                skip = True
            elif word[i + 1] == "e":
                new_word += "a"
                skip = True
        
        elif word[i] == "e":
            if skip:
                skip = False
            elif i == 0:
                new_word += "a"
            elif i == len(word) - 1:
                new_word += "h"
            elif word[i + 1] == "e" or word[i + 1] == "a":
                new_word += "a"
                skip = True
        
        else:
            new_word += word[i]
    
    return new_word



# while(True):
#     word = input("Enter your Hebrew word: ")
#     print("\nYou entered: " + word)
#     print("This was converted to: " + convertToMachineTransliteration(word))