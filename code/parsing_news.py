from urllib.request import urlopen  # Library for urlopen
from bs4 import BeautifulSoup  # Library for html parser (scraper), lxml is also nice
from code.stemming_article import stemming_article
import datetime
import time
import json

site = 'https://www.rt.com'
category_path='business'

#wsj_econ = urlopen(site + '/' + category_path).read().decode('utf-8', 'ignore')  # Making url, reading web-page and converting it to utf-8
wsj_econ = urlopen('http://bogdan.co/BusinessRT.html').read().decode('utf-8', 'ignore')  # Making url, reading web-page and converting it to utf-8
wsj_econ_source = BeautifulSoup(wsj_econ, "html.parser")  # Converting to BS type
wsj_econ_source_urls = BeautifulSoup(str(wsj_econ_source.find_all('div', class_="media__image")), "html.parser")  # finding all pics with news link
final_links = []  # Creating empty array for links
for link in wsj_econ_source_urls.find_all('a'):  # Through loop searching for links
    final_links.append(site + link.get('href'))  # Putting them to the array
i = 0  # Creating an empty variable for an increment to dot all articles' numbers
final_articles = {'articles_data': []}  # Creating empty JSON array for articles
for url_article in final_links:  # Through loop searching for articles' text
    pre_source_article = urlopen(url_article).read().decode('utf-8', 'ignore')  # Reading pages
    source_article = BeautifulSoup(pre_source_article, "html.parser")  # Converting to BS type
    text_article = BeautifulSoup(str(source_article.find_all('div', class_="article__text text ")),
                                 "html.parser")  # searching for articles' text
    temp_article = text_article.text
    temp_published_time = BeautifulSoup(str(source_article.find_all('time', class_="date date_article-header", limit=1)), "html.parser").text
    for ch in ['\'', '\n','\\n', '  ', '\\', '\\', '"', '’', '‘', '“', '”', ']', '[', '/']:
        if ch in temp_article:
            temp_article = temp_article.replace(ch, '')
            temp_published_time = temp_published_time.replace(ch, '')
    temp_article = temp_article.replace(r'\\', r'   ')
    final_articles['articles_data'].append({
        'article_number': i,
         # 'article_time_creation': datetime.datetime.utcnow().isoformat(),
        'published_time' : temp_published_time.replace('Published time: ', ''),
        'source_text': temp_article,
        'stemmed_text': stemming_article(temp_article),
        'url': url_article
    })
    print('.')  # loading string
    i += 1
with open("/home/bogdan/PycharmProjects/graduate_work/data/news2/"+ time.strftime("%d_%m_%Y_%H_%M") + ".json", "w") as text_file:
    print(json.dumps(final_articles), file=text_file)