def stemming_article_2(article):
    import nltk
    from nltk.stem.porter import PorterStemmer
    for_removing = "№#©@&%\\\/=+/~^*,.;:\"'`“”‘’–-—_{}[]()1234567890!@#?$"
    for i in range(0, len(for_removing)):
        article = article.replace(for_removing[i], "")
    article=article.lower()
    filtered = nltk.word_tokenize(article)
    stemmed = []
    for f in filtered:
        stemmed.append(PorterStemmer().stem(f))

    return stemmed