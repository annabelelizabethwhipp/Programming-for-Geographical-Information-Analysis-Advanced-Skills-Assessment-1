"""
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M Programming-for-Spatial-Analysts-Advanced-Skills
    Author: Annabel Whipp
    File name: NLTK.py
    
"""

# imports
import nltk
import os
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from nltk.tokenize import PunktSentenceTokenizer
nltk.download('punkt')

# open file
f = open("poem.txt", "r")

# tokenise poem
tokens = nltk.word_tokenize(f.read())
words = [w.lower() for w in tokens]
text = nltk.Text(tokens)

# nltk function which gives you the frequency of words
fdist1 = FreqDist(tokens)

# Words of length 10
long_words = [w for w in words if len(w) > 10]
# The lengths of words
word_lengths = FreqDist(len(w) for w in tokens)

# pos tagging
tagged = pos_tag(text)
print(tagged)

# the twenty most common words that occur
print("Twenty most common occurances: ", fdist1.most_common(20))

# the words of length 10
print("Words of length 10: ", long_words) 

# pass the most common 20 of word lengths.
print("Most common word lengths: ", word_lengths.most_common(20)) 

