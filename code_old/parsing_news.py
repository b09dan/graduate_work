def parsing_news(site, category_path):
    from urllib.request import urlopen  # Library for urlopen
    from bs4 import BeautifulSoup  # Library for html parser (scraper), lxml is also nice
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
               "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
               "twentyone", "twentytwo", "twentythree", "twentyfour", "twentyfive", "twentysix", "twentyseven",
               "twentyeight", "twentynine", "thirty", "thirtyone", "thirtytwo", "thirtythree", "thirtyfour",
               "thirtyfive", "thirtysix", "thirtyseven", "thirtyeight", "thirtynine", "forty", "fortyone", "fortytwo",
               "fortythree", "fortyfour", "fortyfive", "fortysix", "fortyseven", "fortyeight", "fortynine", "fifty",
               "fiftyone", "fiftytwo", "fiftythree", "fiftyfour", "fiftyfive", "fiftysix", "fiftyseven", "fiftyeight",
               "fiftynine", "sixty", "sixtyone", "sixtytwo", "sixtythree", "sixtyfour", "sixtyfive", "sixtysix",
               "sixtyseven", "sixtyeight", "sixtynine", "seventy", "seventyone", "seventytwo", "seventythree",
               "seventyfour", "seventyfive", "seventysix", "seventyseven", "seventyeight", "seventynine", "eighty",
               "eightyone", "eightytwo", "eightythree", "eightyfour", "eightyfive", "eightysix", "eightyseven",
               "eightyeight", "eightynine", "ninety", "ninetyone", "ninetytwo", "ninetythree", "ninetyfour",
               "ninetyfive", "ninetysix", "ninetyseven", "ninetyeight", "ninetynine",
               "hundred", ]  # Array for numerating articles

    wsj_econ = urlopen(site + '/' + category_path).read().decode('utf-8',
                                                                 'ignore')  # Making url, reading web-page and converting it to utf-8
    wsj_econ_source = BeautifulSoup(wsj_econ, "html.parser")  # Converting to BS type
    wsj_econ_source_urls = BeautifulSoup(str(wsj_econ_source.find_all('div', class_="media__image")),
                                         "html.parser")  # finding all pics with news link
    final_links = []  # Creating empty array for links
    for link in wsj_econ_source_urls.find_all('a'):  # Through loop searching for links
        final_links.append(site + link.get('href'))  # Putting them to the array
    i = 0  # Creating an empty variable for an increment to dot all articles' numbers
    final_articles = []  # Creating empty array for articles
    for url_article in final_links:  # Through loop searching for articles' text
        pre_source_article = urlopen(url_article).read().decode('utf-8', 'ignore')  # Reading pages
        source_article = BeautifulSoup(pre_source_article, "html.parser")  # Converting to BS type
        text_article = BeautifulSoup(str(source_article.find_all('div', class_="article__text text ")),
                                     "html.parser")  # searching for articles' text
        final_articles.append('Article number ' + numbers[i] + ':\n' + text_article.text)  # putting it to array
        i += 1;
        print('.')  # loading string
        print('Downloading File FooFile.txt [%d%%]\r' % i, end="")
    return final_articles

from parsing_news import parsing_news
a=parsing_news('https://www.rt.com','business')
print(a)

