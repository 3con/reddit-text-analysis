"""Builds tf-idf vector matrix of top features in corpus, and labels data
with binary values of low score, high score, and gilded status. Then finds
most used features in each category and prints them."""

import heapq
from load_data import corpus, comments_dict
from stop_words import stop_words
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS


# build tf-idf vector matrix
custom_stop_words = ENGLISH_STOP_WORDS.union(stop_words)

tf = TfidfVectorizer(analyzer='word', max_features=1000, min_df = 0,
                     ngram_range=(3,4), stop_words = custom_stop_words)

tfidf_matrix =  tf.fit_transform(corpus)
phrases = tf.get_feature_names()

dense = tfidf_matrix.todense()


# build list of lists, with each element representing one comment
#       and containing tuples of (feature_name index, tf-idf value)
phrases_by_comment = []

for i in range(0, len(dense)):
    comment = dense[i].tolist()[0]
    phrase_scores = [pair for pair in zip(range(0, len(comment)), comment)]
    phrases_by_comment.append(phrase_scores)


# build 3 dictionaries counting occurrences of popular phrases
low_counts, high_counts, gilded_counts = {}, {}, {}
k = 0

for comment in phrases_by_comment:
    if comments_dict[k]['low'] == 1:
        for phrase in comment:
            low_counts[phrase[0]] = low_counts.get(phrase[0], 0) + phrase[1]

    elif comments_dict[k]['high'] == 1:
        for phrase in comment:
            high_counts[phrase[0]] = high_counts.get(phrase[0], 0) + phrase[1]
    
    if comments_dict[k]['gilded'] == 1:
        for phrase in comment:
            gilded_counts[phrase[0]] = gilded_counts.get(phrase[0], 0) + phrase[1]
    k += 1


# find most common phrase indexes in each category
n = 5

low_indexes = heapq.nlargest(n, low_counts, key=low_counts.get)
high_indexes = heapq.nlargest(n, high_counts, key=high_counts.get)
gilded_indexes = heapq.nlargest(n, gilded_counts, key=gilded_counts.get)


# translate index to phrase
low_phrases = [phrases[i] for i in low_indexes]
high_phrases = [phrases[i] for i in high_indexes]
gilded_phrases = [phrases[i] for i in gilded_indexes]


# print output
print "Downvoted phrases: " + ", ".join(low_phrases)
print "Upvoted phrases: " + ", ".join(high_phrases)
print "Gilded phrases: " + ", ".join(gilded_phrases)
