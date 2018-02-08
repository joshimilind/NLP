import nltk
from nltk.corpus import webtext

print(webtext.fileids())

fileid = 'singles.txt'
wbt_words = webtext.words(fileid)
fdist = nltk.FreqDist(wbt_words)
print('Count of max appearing tokens "',fdist.max(),'" : ', fdist[fdist.max()])

# distinct words
print('Total no of distinct tokens in the bag : ',fdist.N())
# most common words
print('most common words : ',fdist.most_common(10))
# tabulate data
print('Frequency distribution on ad :')
print(fdist.tabulate())
fdist.plot(cumulative=True)
