from load_data import corpus
from sklearn.feature_extraction.text import TfidfVectorizer

tf = TfidfVectorizer(analyzer='word', max_features=100, min_df = 0, ngram_range=(1,3), stop_words = 'english')

tfidf_matrix =  tf.fit_transform(corpus)
feature_names = tf.get_feature_names()

dense = tfidf_matrix.todense()

phrases_by_comment = []

for i in range(0, len(dense)):
    comment = dense[i].tolist()[0]
    phrase_scores = [pair for pair in zip(range(0, len(comment)), comment) if pair[1] > 0]
    phrases_by_comment.append(phrase_scores)

print phrases_by_comment

## output: [[(68, 0.7016522097362441), (95, 0.7125195973250462)],   < first comment
##          [(56, 1.0)],                                            < second comment...
##          [],
##          [(2, 0.5627634875214949), (18, 0.4863293890204364), (50, 0.40534376325697624), (80, 0.5314860450438239)],
##          ...]
