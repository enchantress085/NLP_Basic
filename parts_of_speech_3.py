# -*- coding: utf-8 -*-

import nltk

paragr = """It is this fate, I solemnly assure you, that I dread for you,
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
               pay the penalty for it. """
               
               
words = nltk.word_tokenize(paragr)
tagged_words = nltk.pos_tag(words)

words_tag = []
for tw in tagged_words:
    words_tag.append(tw[0]+"__"+tw[1])
tagged_paragraph = ' '.join(words_tag)



### Importent 
""" 
Here are the meanings of the Parts-Of-Speech tags used in NLTK

CC -- Coordinating conjunction

CD -- Cardinal number

DT -- Determiner

EX -- Existential there

FW -- Foreign word

IN

Preposition or subordinating conjunction

JJ

Adjective

JJR

Adjective, comparative

JJS

Adjective, superlative

LS

List item marker

MD

Modal

NN

Noun, singular or mass

NNS

Noun, plural

NNP

Proper noun, singular

NNPS

Proper noun, plural

PDT

Predeterminer

POS

Possessive ending

PRP

Personal pronoun

PRP$

Possessive pronoun

RB

Adverb

RBR

Adverb, comparative

RBS

Adverb, superlative

RP

Particle

SYM

Symbol

TO

to

UH

Interjection

VB

Verb, base form

VBD

Verb, past tense

VBG

Verb, gerund or present participle

VBN

Verb, past participle

VBP

Verb, non-3rd person singular present

VBZ

Verb, 3rd person singular present

WDT

Wh-determiner

WP

Wh-pronoun

WP$

Possessive wh-pronoun

WRB

Wh-adverb
"""


