import nltk
# nltk.download('brown')
from nltk.corpus import brown

print('categories are : ')
print(brown.categories())

genres = ['fiction', 'humor', 'romance']
whwords = ['what', 'who', 'where', 'which', 'how', 'why', 'when', 'when']
# whwords = ['what', 'who']


for whword in range(0, len(genres)):
    genre = genres[whword]
    print()
    print("analysing '" + genre + "' whwords")
    genre_text = brown.words(categories=genre)
    fdist = nltk.FreqDist(genre_text)
    for wh in whwords:
        print(wh + ':', fdist[wh], end=' ')
        print()
