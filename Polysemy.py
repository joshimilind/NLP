from nltk.corpus import wordnet as wn
def calculatePolysemy():
    calculatePolysemy = ['n', 'v', 'r', 'a']
    for i in calculatePolysemy:
        type = i
        synsets = wn.all_synsets(type)
        lemmas = []
        for synset in synsets:
            for lemma in synset.lemmas():
                lemmas.append(lemma.name())
        lemmas = set(lemmas)
        count = 0
        for lemma in lemmas:
            count = count + len(wn.synsets(lemma, type))
        print('Total distinct lemmas: ', len(lemmas))
        print('Total senses : ', count)
        print('Average polysemy of ', type, ': ', count/len(lemmas), '\n')

calculatePolysemy()
