from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def clean(text):

    customList = [",", "'s", ".", "n't", "like", "'re", "'m", 'music']
    data = text.lower()
    # data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
    swords = stopwords.words('english')
    for word in customList:
        swords.append(word)
    stopWords = set(swords)
    words = word_tokenize(data)
    wordsFiltered = []

    for w in words:
        if w not in stopWords and ( w != '[' and w != ']'):
            wordsFiltered.append(w)
    return wordsFiltered