'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M Programming-for-Spatial-Analysts-Advanced-Skills
    Author: Annabel Whipp
    File name: NLTK.py
    
'''

# imports
import nltk
import os
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from nltk.tokenize import PunktSentenceTokenizer

nltk.download('punkt')


f = open("poem.txt", "r")

tokens = nltk.word_tokenize(f.read())
words = [w.lower() for w in tokens]
text = nltk.Text(tokens)

fdist1 = FreqDist(tokens)


# Words of length 10
long_words = [w for w in words if len(w) > 10]
# The lengths of words
word_lengths = FreqDist(len(w) for w in tokens)

#tagged = pos_tag(text)


print("Twenty most common occurances: ", fdist1.most_common(20)) # The twenty most common words that occur.
print("Words of length 10: ", long_words) # The words of length 10.
print("Most common word lengths: ", word_lengths.most_common(20)) # We pass the most common 20 of word lengths.

