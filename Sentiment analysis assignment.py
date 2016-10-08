import nltk
from nltk.corpus import sentiwordnet as swn
from nltk.tokenize import word_tokenize

f = open("/home/abhishek/day4.txt")
lines = f.readlines()

tokens = [word_tokenize(i) for i in lines]

words = list()
for i in tokens:
	for j in i:
		words.append(j)

sentiments = {}
for i in words:
	k = swn.senti_synsets(i)
	if len(k)==0:
		continue
	else:
		if k[0].pos_score() > k[0].neg_score():
			sentiments[i]="positive"
		elif k[0].pos_score() < k[0].neg_score():
			sentiments[i]="negative"
		else:
			sentiments[i]="neutral"


