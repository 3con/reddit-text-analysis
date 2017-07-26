"""Tokenizes, cleans and stems comment text from file, and stores comments
with score and gilded status in comments dictionary. Adds all comments as
elements in corpus array."""

import json
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

def clean_text(text):
    """Makes text lowercase, removes punctuation and formatting,
    and passes text through a stemmer. Returns a string."""

    lowers = text.lower()
    no_punctuation = lowers.translate(None, string.punctuation)
    clean = no_punctuation.replace('rnrn',' ')
    tokens = clean.split()
    stems = stem_tokens(tokens, stemmer)
    return " ".join(stems)


# read data from file
with open("data/RC_2006-01") as f:
    
    content = f.readlines()
    j = 0

    for entry in content:
        json_entry = json.loads(entry)

        comment = clean_text(json_entry["body"].encode('ascii','ignore'))
        score = json_entry["score"]
        low = 1 if score < 0 else 0
        high = 1 if score > 5 else 0
        gilded = json_entry["gilded"]

        comments_dict[j] = {"comment": comment,
                            "score": score,
                            "low": low,
                            "high": high,
                            "gilded": gilded}

        j += 1

corpus = []

for comment in comments_dict:
    corpus.append(comments_dict[comment]["comment"])
