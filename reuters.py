from nltk.corpus import reuters

files = reuters.fileids()
print(files)

# word associated with id 16097
words16097 = reuters.words(['test/16097'])
print()
print(words16097)

# 20 words
words20 = reuters.words(['test/16097'])[:20]
print(words20)

reutersGenres = reuters.categories()
print()
print(reutersGenres)

for word in reuters.words(categories=['bop', 'cocoa']):
    print(word + ' ', end='')
    if word is '.':
        print()
