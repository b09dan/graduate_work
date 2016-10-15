import nltk
from nltk.stem.porter import PorterStemmer
import csv
from collections import defaultdict

columns = defaultdict(list)  # each value in each column is appended to a list

with open('text_sensibility.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=';')
    for row in spamreader:
        for (k, v) in row.items():
            columns[k].append(v)
# print(' '.join(columns['word']))
csvfile.close()

filtered = nltk.word_tokenize(' '.join(columns['word']))
stemmed = []
for f in filtered:
    stemmed.append(PorterStemmer().stem(f))

print(stemmed)

with open("text_sensibility.csv", "w+") as to_file:
    writer = csv.writer(to_file)
    for new_row in stemmed:
        writer.writerow(new_row)
