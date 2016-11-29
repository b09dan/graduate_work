def connecting_function(articles):
    from code.stemming_articles import stemming_articles

    print("Всего получено", len(articles), "статей.")
    i = 0
    articles_sum = []
    for var in articles:
        articles_sum.append(stemming_articles(articles, i))
        # print(stemming_articles(articles, i))
        i += 1
    return articles_sum