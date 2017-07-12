"""Tokenizes, cleans and stems comment text from file, and stores comments
with comment_id, score, and gilded status in comments dictionary. Adds all
comments as elements in corpus array."""

import string
from collections import defaultdict

import nltk
from nltk.stem.porter import PorterStemmer
 

comments_dict = defaultdict(dict)
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    """Stems array of tokenized text using nltk PorterStemmer."""

    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

# def remove_stopwords(tokens):
#     stopwords = [x]
#     no_stopwords = []
#     for item in tokens:
#         if item not in stopwords:
#             no_stopwords.append(item)
#     return no_stopwords

def clean_text(text):
    """Makes text lowercase, removes punctuation and formatting,
    and passes text through a stemmer. Returns a string."""

    lowers = text.lower()
    no_punctuation = lowers.translate(None, string.punctuation)
    clean = no_punctuation.replace('rnrn',' ')
    tokens = clean.split()
    stems = stem_tokens(tokens, stemmer)
    # no_stopwords = remove_stopwords(stems)
    return " ".join(stems)


# def load_data(file):
with open("data/RC_2006-01") as f:
    
    content = f.readlines()
    j = 0

    for entry in content:
        # extract comment id
        start = entry.find('"id":') + 6
        for i, char in enumerate(entry[start:]):
            if char == '"':
                end = i+(start)
                break
        comment_id = entry[start:end]

        # extract comment body
        start = entry.find('"body":') + 8
        for i, char in enumerate(entry[start:]):
            if char == '"' and entry[i+(start)-1] != '\\':
                end = i+(start)
                break
        comment = entry[start:end]
        comment = clean_text(comment)

        # extract comment score (upvotes and downvotes), categorize into low/high
        start = entry.find('"score":') + 8
        for i, char in enumerate(entry[start:]):
            if char == ',':
                end = i+(start)
                break
        score = entry[start:end]
        if score == '':
            score = '0'
        score = int(score)

        low = 1 if score < 0 else 0
        high = 1 if score > 10 else 0

        # extract comment gilded status
        start = entry.find('"gilded":') + 9
        for i, char in enumerate(entry[start:]):
            if char == ',':
                end = i+(start)
                break
        gilded = entry[start:end]

        comments_dict[j] = {"comment": comment,
                            "score": score,
                            "low": low,
                            "high": high,
                            "gilded": gilded}

        j += 1

corpus = []

for comment in comments_dict:
    corpus.append(comments_dict[comment]["comment"])
