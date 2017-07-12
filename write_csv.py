import csv
from load_data import comments_dict
from data_matrix import phrases_by_comment


# write to csv file
with open('sample-dataset.csv', 'wb') as d:
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
##      entries of df values indexed by feature_name,
##      followed by three labels: low, high, and gilded binary values
