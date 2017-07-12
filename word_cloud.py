import csv
from load_data import corpus, comments_dict
from sklearn.feature_extraction.text import TfidfVectorizer


tf = TfidfVectorizer(analyzer='word', max_features=100, min_df = 0, stop_words = 'english')

tfidf_matrix =  tf.fit_transform(corpus)
feature_names = tf.get_feature_names()

dense = tfidf_matrix.todense()

phrases_by_comment = []

for i in range(0, len(dense)):
    comment = dense[i].tolist()[0]
    phrase_scores = [pair for pair in zip(range(0, len(comment)), comment)]
    phrases_by_comment.append(phrase_scores)


# write to csv file
with open('dataset.csv', 'wb') as d:
    writer = csv.writer(d, quoting=csv.QUOTE_MINIMAL)
    j = 0
    for comment in phrases_by_comment:
        row = [0] * len(comment)
        for phrase in comment:
            row[phrase[0]] = phrase[1]
        row.append(comments_dict[j]['low'])
        row.append(comments_dict[j]['high'])
        row.append(comments_dict[j]['gilded'])
        writer.writerow(row)
        j += 1

## output:
## a row for each comment:
##      100 entries of df values indexed by feature_name,
##      followed by three labels: low, high, and gilded binary values.

## next:
## for each row with low=1:
##      find most common words
