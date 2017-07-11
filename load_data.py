from collections import defaultdict
import json
 
comments = defaultdict(dict)

# def load_data(file):
with open("data/RC_2006-01") as f:
    content = f.readlines()

    for entry in content:
        num = entry.find('"id":')
        start = num+6
        for i, char in enumerate(entry[num+6:]):
            if char == '"':
                end = i+(num+6)
                break
        comment_id = entry[start:end]

        num = entry.find('"body":')
        start = num+8
        for i, char in enumerate(entry[num+8:]):
            if char == '"' and entry[i+(num+7)] != '\\':
                end = i+(num+8)
                break
        comment = entry[start:end]

        num = entry.find('"score":')
        start = num+8
        for i, char in enumerate(entry[num+8:]):
            if char == ',':
                end = i+(num+8)
                break
        score = entry[start:end]
        if score == '':
            score = '0'
        score = int(score)

        comments[comment_id] = {"comment": comment,
                                "score": score}

corpus = []

for comment in comments:
    corpus.append(comments[comment]["comment"])
