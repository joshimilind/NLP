import nltk
from nltk.corpus import wordnet as wn
# nltk.download('wordnet')

chair = 'chair'
chair_synsets = wn.synsets(chair)
print('Synsets/Sense of chair : ', chair_synsets, '\n\n')
for synset in chair_synsets:
    print(synset, ' : ')
    print('Definition : ', synset.definition())
    print('Lemmas/Synonymous words : ', synset.lemma_names())
    print('Example : ', synset.examples(), '\n')

