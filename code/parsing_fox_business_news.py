from urllib.request import urlopen  # Library for urlopen
from bs4 import BeautifulSoup  # Library for html parser (scraper), lxml is also nice
from code.stemming_article import stemming_article
import datetime
import time
import json

site = 'http://www.foxbusiness.com'

#wsj_econ = urlopen(site + '/' + category_path).read().decode('utf-8', 'ignore')  # Making url, reading web-page and converting it to utf-8
wsj_econ = urlopen('https://testsite.bogdan.co/Stocks_Category.html').read().decode('utf-8', 'ignore')  # Making url, reading web-page and converting it to utf-8
wsj_econ_source = BeautifulSoup(wsj_econ, "html.parser")  # Converting to BS type
wsj_econ_source_urls = BeautifulSoup(str(wsj_econ_source.find_all('div', class_="info")), "html.parser")  # finding all pics with news link
final_links = []  # Creating empty array for links
for link in wsj_econ_source_urls.find_all('a'):  # Through loop searching for links
    final_links.append(site + link.get('href'))  # Putting them to the array
    #xxprint(site + link.get('href'))
i = 0  # Creating an empty variable for an increment to dot all articles' numbers
final_articles = {'articles_data': []}  # Creating empty JSON array for articles
for url_article in final_links:  # Through loop searching for articles' text
    try:
        pre_source_article = urlopen(url_article).read().decode('utf-8', 'ignore')  # Reading pages
        source_article = BeautifulSoup(pre_source_article, "html.parser")  # Converting to BS type

        temp_article = BeautifulSoup(str(source_article.find_all('div', class_="article-text")),
                                     "html.parser").text  # searching for articles' text

        temp_published_time = BeautifulSoup(str(source_article.find('time')), "html.parser").find('time').attrs[
            'datetime']

        temp_theme = BeautifulSoup(str(source_article.find('span', class_="tags")), "html.parser").find('a').text

        for ch in ['\'', '\n','\\n', '  ', '\\', '\\', '"', '’', '‘', '“', '”', ']', '[', '/']:
            if ch in temp_article:
                temp_article = temp_article.replace(ch, '')
                temp_published_time = temp_published_time.replace(ch, '')
        temp_article = temp_article.replace(r'\\', r'   ')
        final_articles['articles_data'].append({
            'article_number': i,
            'theme': temp_theme,
            'published_time' : temp_published_time.replace('Published time: ', ''),
            'source_text': temp_article,
            'stemmed_text': stemming_article(temp_article),
            'url': url_article
        })
        print(str(i)+"/"+str(len(final_links)))  # loading string
        i += 1
    except:
        print("Упс, ошибочка!")
        i += 1
with open("/home/bogdan/PycharmProjects/graduate_work/data/fox_business/"+ time.strftime("%d_%m_%Y_%H_%M") + ".json", "w") as text_file:
    print(
        json.dumps(
            final_articles,
            indent=4,
            sort_keys=True
        ),
        file=text_file
    )
