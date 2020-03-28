# -*- coding: utf-8 -*-

import nltk
paragraph = """ The Taj Mahal was built by Emperor Shah Jahan."""



words = nltk.word_tokenize(paragraph)
tagged_words = nltk.pos_tag(words)

nameEntity = nltk.ne_chunk(tagged_words)
nameEntity.draw()



"""

ORGANIZATION	Georgia-Pacific Corp., WHO
PERSON	Eddy Bonte, President Obama
LOCATION	Murray River, Mount Everest
DATE	June, 2008-06-29
TIME	two fifty a m, 1:30 p.m.
MONEY	175 million Canadian Dollars, GBP 10.40
PERCENT	twenty pct, 18.75 %
FACILITY	Washington Monument, Stonehenge
GPE	South East Asia, Midlothian 

"""