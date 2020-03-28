# -*- coding: utf-8 -*-
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
import nltk
#text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

text = """It has finally happened, you guys. We have witnessed a historic moment. Well, we witnessed many historic moments, but Leonardo DiCaprio winning an Oscar for the first time just felt like a victory for all of us, you know? DiCaprio has been nominated for an Oscar so many times, only to go home empty-handed, that it has reached meme levels. So to see him finally stand on that stage with a golden statue in his hand was just so heartwarming. Unsurprisingly, when you look at the transcript of DiCaprio's Oscar acceptance speech (which he must surely have been planning for the last 10 years), you see how it's not just thanking people and then breezing off the stage. No, the 41-year-old actor took a moment to speak about a cause that's very close to his heart: environmentalism and climate change.
I mean, don't get me wrong. DiCaprio did thank a lot of people, some of them collectively. (Like his friends. "You know who you are.") But working on The Revenant highlighted a cause that DiCaprio supports when the cameras stop rolling, and he wasn't going to let that go unmentioned in his speech. Not when he finally had the eyes of the world upon him for more than just making Sad Leo at the Oscars GIFs. Reading his speech should be enough to inspire fans to give environmentalism the same attention that we've given to DiCaprio's numerous losses over the years. However, even if it doesn't, the fact that he would draw attention away from himself and toward a good cause is just so DiCaprio that it really makes me feel like he deserved this award for more than one reason."""

n = 3
ngram = {} #Dictionary
words = nltk.word_tokenize(text)

# Create n- gram 
for i in range(len(words)-n):
    gram = ' '.join(words[i:i+n])
    if gram not in ngram.keys():
        ngram[gram] = []
    ngram[gram].append(words[i+n])
    
# Testing word n-gram models  
currentgram = ' '.join(words[0:n])
result = currentgram
for i in range(30):
    if currentgram not in ngram.keys():
        break 
    possibilities = ngram[currentgram]
    nextitem = possibilities[random.randrange(len(possibilities))]
    result += ' '+nextitem
    rwords = nltk.word_tokenize(result)
    currentgram = ' '.join(rwords[len(rwords)-n:len(rwords)])
print(result)






















