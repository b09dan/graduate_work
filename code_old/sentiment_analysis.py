def sentiment_analysis(day):
    import csv
    from collections import defaultdict
    import numpy as np
    from code.xml_2_array import xml_2_array

    day_array = xml_2_array(day)  # receiving a two dimensional array of articles

    columns = defaultdict(list)  # each value in each column is appended to a list
    with open('dicts/text_sensibility_almost_new.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=';')
        for row in spamreader:
            for (k, v) in row.items():
                columns[k].append(v)
    Matrix = [[0 for x in range(3)] for x in range(len(columns['word']))]  # Two-dimensional array of dictionary
    for i in range(len(Matrix)):
        Matrix[i][0] = columns['stemmed'][i]
        Matrix[i][1] = columns['negative'][i]
        Matrix[i][2] = columns['positive'][i]
    words_column = np.array(Matrix)[:, 0].tolist()  # Taking the first column (with stemmed words) from our matrix
    negative_column = np.array(Matrix)[:, 1].tolist()  # Taking the first column (with negative index) from our matrix
    positive_column = np.array(Matrix)[:, 2].tolist()  # Taking the first column (with positive index) from our matrix

    # Check
    # with open("check.csv", "a", encoding='utf-8') as myfile:
    #     myfile.write(str(positive_column))
    positive = 0
    negative = 0
    error = 0
    for i in range(0, len(day_array)):
        for j in range(0, len(day_array[i])):
            try:
                word_index = words_column.index(day_array[i][j])
                negative += float(negative_column[word_index].replace(',', '.'))
                positive += float(positive_column[word_index].replace(',', '.'))
            except ValueError:
                error += 1
    print("Error (not found) amount: ", error)
    print("Positive amount in words: ", positive, "Percentage: ", positive/sum(len(x) for x in day_array))
    print("Negative amount in words: ", negative, "Percentage: ", negative/sum(len(x) for x in day_array))
    print("Total amount: ", sum(len(x) for x in day_array))


