# Some theory: http://scialert.net/fulltext/?doi=tasr.2011.1141.1157&org=10
# lib url: http://textblob.readthedocs.org/en/dev/api_reference.html#module-textblob.en.sentiments
# also some detailed tutorial for Bayes classification: http://andybromberg.com/sentiment-analysis-python/#fnref:1
from os import walk
import json
# For graphics
import numpy as np
import matplotlib.pyplot as plt

from textblob import TextBlob

dir = "/home/bogdan/PycharmProjects/graduate_work/data/news2/"
report_name = input('Please, enter report name: ')
files_with_news = []
for (dirpath, dirnames, filenames) in walk(dir):
    files_with_news.extend(filenames)
    break
polarities_4_plot = []
with open("/home/bogdan/PycharmProjects/graduate_work/data/news_analysis/"+report_name+".csv", "w", encoding='utf-8') as myfile:
    myfile.write('date_time_utc_iso;polarity;url\n')
    for news_day_file in files_with_news:
        with open(dir+news_day_file) as json_file:
            json_file = json.load(json_file)
            for article_in_file in json_file['articles_data']:
                temp_sentiment = TextBlob(article_in_file['source_text']).sentiment[0]
                myfile.write(article_in_file['published_time'] + ';' + str(temp_sentiment) + ';' + article_in_file['url']+ '\n')
                polarities_4_plot.append(temp_sentiment)

y = np.asarray(polarities_4_plot)
x = np.arange(0, len(y), 1)

plt.axis([0.0,len(y)+1, min(y)-0.01,max(y)+0.01])
ax = plt.gca()
ax.set_autoscale_on(False)
plt.plot(x, y)
plt.legend(['Тональности новостей'])
plt.show()

