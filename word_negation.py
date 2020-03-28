# -*- coding: utf-8 -*-
# ----------- Word Negation 

import nltk
from nltk.corpus import wordnet
text = "They do not go to school on Wednesday afternoons."

words = nltk.word_tokenize(text)

new_words = []
temp_word = ""

"""for word in words:
    if word == "not":
        temp_word = "not_"
    elif temp_word == "not_":
        word = temp_word + word
        temp_word = ""
    if word != "not":
        new_words.append(word)"""

for word in words:
    antonyms = []
    if word == "not":
        temp_word = "not_"
    elif temp_word == "not_":
        for syn in wordnet.synsets(word):
            for s in syn.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
        if len(antonyms) >= 1:
            word = antonyms[0]
        else:
            word = temp_word + word
        temp_word = ""
    if word != "not":
      new_words.append(word)
    
    
text = ' '.join(new_words)
    
    
    