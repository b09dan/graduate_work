def getting_sentiment_coefficients_list():
    from os import walk
    from code.sentiment_analysis import sentiment_analysis
    files_with_news = []
    for (dirpath, dirnames, filenames) in walk('news/'):
        files_with_news.extend(filenames)
        break
    for news_day in files_with_news:
        print(news_day)
        sentiment_analysis(news_day)
    # return files_with_news


getting_sentiment_coefficients_list()

