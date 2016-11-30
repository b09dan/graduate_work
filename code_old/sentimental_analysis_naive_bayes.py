# Some theory: http://scialert.net/fulltext/?doi=tasr.2011.1141.1157&org=10
# lib url: http://textblob.readthedocs.org/en/dev/api_reference.html#module-textblob.en.sentiments
# also some detailed tutorial for Bayes classification: http://andybromberg.com/sentiment-analysis-python/#fnref:1
from os import walk

from textblob import TextBlob

from xml_2_array import xml_2_array

dir = input('Enter files directory: ')
report_name = input('Please, enter report name: ')
files_with_news = []
for (dirpath, dirnames, filenames) in walk(dir):
    files_with_news.extend(filenames)
    break
polarities_4_plot = []
with open("news_analysis/"+report_name+".csv", "w", encoding='utf-8') as myfile:
    myfile.write('day;article_number;polarity\n')
    for news_day in files_with_news:
        wiki = xml_2_array(dir.replace('news/', '') +news_day)
        for i in range(0, len(wiki)):
            wiki[i] = ' '.join(wiki[i])
        # print(news_day.replace('.xml', ''))
        for i in range(0, len(wiki)):
            wiki[i] = TextBlob(wiki[i])
            # print('Article №', i, ': ', wiki[i].sentiment)
            myfile.write(news_day.replace('.xml', '') + ';' +
                         'article_' + str(i + 1) + ';' +
                         str(wiki[i].sentiment[0]) + '\n'
                         )
            polarities_4_plot.append(wiki[i].sentiment[0])
print(polarities_4_plot)
import numpy as np
import matplotlib.pyplot as plt

y = np.asarray(polarities_4_plot)
x = np.arange(0, len(y), 1);

plt.axis([0.0,len(y)+1, min(y)-0.01,max(y)+0.01])
ax = plt.gca()
ax.set_autoscale_on(False)
plt.plot(x, y)
plt.legend(['Probability distribution'])
plt.show()