from load_data import corpus
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np


cv = CountVectorizer(analyzer='word', max_features=200, min_df=0, stop_words="english")
counts = cv.fit_transform(corpus).toarray().ravel()
words = np.array(cv.get_feature_names())

# normalize
counts = counts / float(counts.max())
