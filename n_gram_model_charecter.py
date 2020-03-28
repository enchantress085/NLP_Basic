# -*- coding: utf-8 -*-
"""
 ------- What are N-grams used for? --------

N-grams are used for a variety of different task.
For example, when developing a language model, 
n-grams are used to develop not just unigram 
models but also bigram and trigram models.
 
Google and Microsoft have developed web scale n-gram 
models that can be used in a variety of tasks such as 

  1. spelling correction, 
  2. word breaking,
  3. text summarization
 
Here is a publicly available web scale n-gram model by 
  **. Microsoft: http://research.microsoft.com/en-us/collaboration/focus/cs/web-ngram.aspx. 
Here is a paper that uses Web N-gram models for text summarization:
  
  **. Micropinion Generation: An Unsupervised Approach to Generating 
   Ultra-Concise Summaries of Opinions.

Another use of n-grams is for developing features for 
supervised Machine Learning models such as 
1. SVMs, 
2. MaxEnt models, 
3. Naive Bayes, etc. 

The idea is to use tokens such as bigrams in the feature space instead 
of just unigrams. 
"""

# N - Gram models 
import random

text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

n = 6
ngram = {} #Dictionary

# Create n- gram 
for i in range(len(text)-n):
    gram = text[i:i+n] # text[0:3] = glo
    if gram not in ngram.keys():
        ngram[gram] = []
    ngram[gram].append(text[i+n]) #text[0+3] = b
    
# Testing n-gram models 
currentgram = text[0:n]
result = currentgram

for i in range(200):
    if currentgram not in ngram.keys():
        break
    possibilities = ngram[currentgram]
    nextitem = possibilities[random.randrange(len(possibilities))]
    result += nextitem
    currentgram = result[len(result)-n:len(result)]
print(result)

    





















