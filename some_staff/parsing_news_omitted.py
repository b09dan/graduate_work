from connecting_function import connecting_function
from lxml import etree
import time
import datetime

def parsing_news_omitted():
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
    final_links = [] # Creating empty array for links
    while 1:
        temp_url_input = input("url: ")
        if temp_url_input == ".":
            break
        else:
            final_links.append(temp_url_input)
    i = 0
    final_articles = []  # Creating empty array for articles
    for url_article in final_links:  # Through loop searching for articles' text
        pre_source_article = urlopen(url_article).read().decode('utf-8', 'ignore')  # Reading pages
        source_article = BeautifulSoup(pre_source_article, "html.parser")  # Converting to BS type
        text_article = BeautifulSoup(str(source_article.find_all('div', class_="article__text text ")),
                                     "html.parser")  # searching for articles' text
        final_articles.append('Article number ' + numbers[i] + ':\n' + text_article.text)  # putting it to array
        i += 1;
        print('.')  # loading string
    return final_articles

omitted_month = int(input("Please enter the number of omitted month: "))
omitted_day = int(input("Please enter the number of omitted day: "))
current_year = int(datetime.datetime.now().strftime("%Y"))
current_date = datetime.date(current_year, omitted_month, omitted_day)


a = connecting_function(parsing_news_omitted())

root = etree.Element("parsed")
etree.tostring(root)
sub_root = etree.Element("news_for_today", date=current_date.strftime("%d") + "." + current_date.strftime(
        "%m") + "." + current_date.strftime("%Y"),
                         time=time.strftime("%H:%M:%S"))
root.append(sub_root)

for i in range(0, len(a)):
    etree.SubElement(sub_root, "article", number=str(i)).text = str(a[i])

handle = str(etree.tostring(root, encoding='utf-8', xml_declaration=False, pretty_print=False))
handle = handle.replace('b\'', '')
handle = handle.replace('\'', '')
handle = handle.replace('  ', '')
handle = handle.replace('\\', '')
with open("../news/" + current_date.strftime("%B") + "/" + current_date.strftime("%d") + "_" + current_date.strftime(
        "%m") + "_" + current_date.strftime("%Y") + ".xml",
          "w") as text_file:
    print(handle, file=text_file)
