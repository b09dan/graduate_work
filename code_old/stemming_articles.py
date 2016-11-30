def stemming_articles(articles, j):
    import nltk
    from nltk.stem.porter import PorterStemmer
    line = articles[j]
    for_removing = "№#©@&%\\\/=+/~^*,.;:\"'`“”‘’–-—_{}[]()1234567890!@#?$"
    for i in range(0, len(for_removing)):
        line = line.replace(for_removing[i], "")
    line=line.lower()
    filtered = nltk.word_tokenize(line)
    stemmed = []
    for f in filtered:
        stemmed.append(PorterStemmer().stem(f))

    return stemmed

