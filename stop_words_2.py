# -*- coding: utf-8 -*-

#Problem this file 

import nltk

from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords


paragraph = """It is this fate, I solemnly assure you, that I dread for you,
               when the time comes that you make your reckoning, and realize 
               that there is no longer anything that can be done. May you never 
               find yourselves, men of Athens, in such a position! Yet in any 
               case,it were better to die ten thousand deaths, than to do anything 
               out of servility towards Philip [or to sacrifice any of those 
               who speak for your good]. A noble recompense did the people in 
               Oreus receive, for entrusting themselves to Philip’s friends, 
               and thrusting Euphraeus aside! And a noble recompense the 
               democracy of Eretria, for driving away your envoys, and 
               surrendering to Cleitarchus! They are slaves, scourged and 
               butchered! A noble clemency did he show to the Olynthians, 
               who elected Lasthenes to command the cavalry, and banished 
               Apollonides! It is folly, and it is cowardice, to cherish 
               hopes like these, to give way to evil counsels, to refuse to 
               do anything that you should do, to listen to the advocates of 
               the enemy’s cause, and to fancy that you dwell in so great a 
               city that, whatever happens, you will not suffer any harm.And 
               I am sure that all would agree, however little they may act on 
               their belief, that our aim, both in speech and in action, 
               should be to cause him to cease from his insolence and to 
               pay the penalty for it."""
               

#Stop_words 
sentence = nltk.sent_tokenize(paragraph)

for i in range(len(sentence)):
    words = nltk.word_tokenize(sentence[i])
    newwords = [word for word in words if word not in stopwords.words('english')]
    sentence = ' '.join(newwords)
