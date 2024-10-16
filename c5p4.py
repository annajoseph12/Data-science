print("SJC23MCA-2017 : Anna S")
print("Batch : MCA 2023-25")
from nltk import ngrams
sentence='I reside in India'
n=3
trigrams=ngrams(sentence.split(),n)
for grams in trigrams:
    print(grams)