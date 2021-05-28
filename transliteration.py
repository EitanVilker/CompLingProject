
# Transliterated Hebrew to Hebrew rules
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
# l -> ל
# m -> מ
# n -> נ
# n (final) -> ן
# s -> ס
# y -> ע 
# p -> פ
# p (final) -> ף
# q -> ק
# r -> ר
# e -> ש
# t -> ת



def convertToMachineTransliteration(word):

    new_word = ""
    skip = False
    for i in range(len(word)):
        
        if word[i] == "s":
            if i < len(word) and word[i + 1] == "h":
                new_word += "e"
                skip = True
            else:
                new_word += "s"
        
        elif word[i] == "c":
            if i < len(word) and word[i + 1] == "h":
                new_word += "x"
                skip = True
            else:
                new_word += "k"
        
        elif word[i] == "k":
            if i < len(word) and word[i + 1] == "h":
                new_word += "x"
                skip = True
            else:
                new_word += "k"

        elif word[i] == "h":
            if (skip):
                skip = False
            else:
                new_word += "h"
        
        elif word[i] == "b":
            new_word += "b"
        
        elif word[i] == "g":
            new_word += "g"
        
        elif word[i] == "v":
            new_word += "w"
        
        elif word[i] == "z":
            new_word += "z"
        
        elif word[i] == "t":
            new_word += "t"
        
        elif word[i] == "y":
            new_word += "i"
        
        elif word[i] == "l":
            new_word += "l"
        
        elif word[i] == "m":
            new_word += "m"
        
        elif word[i] == "n":
            new_word += "n"
        
        elif word[i] == "p":
            new_word += "p"

        elif word[i] == "f":
            new_word += "p"
        
        elif word[i] == "r":
            new_word += "r"