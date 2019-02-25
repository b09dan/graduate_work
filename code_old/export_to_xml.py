from parsing_news import parsing_news

from connecting_function import connecting_function

try:
    import xml.etree.cElementTree as etree
except ImportError:
    import xml.etree.ElementTree as etree
import datetime
import time
print("news/" +datetime.datetime.now().strftime("%B")+"/"+ time.strftime("%d/%m/%Y").replace('/', '_') + ".xml")
a = connecting_function(parsing_news('https://www.rt.com', 'business'))

root = etree.Element("parsed")
etree.tostring(root)
sub_root = etree.Element("news_for_today", date=time.strftime("%d/%m/%Y").replace('/', '.'),
                         time=time.strftime("%H:%M:%S"))
root.append(sub_root)

for i in range(0, len(a)):
    etree.SubElement(sub_root, "article", number=str(i)).text = str(a[i])

handle = str(etree.tostring(root, encoding='utf-8')) #xml_declaration=False, pretty_print=False
handle = handle.replace('b\'', '')
handle = handle.replace('\'', '')
handle = handle.replace('  ', '')
handle = handle.replace('\\', '')

with open("/home/bogdan/PycharmProjects/graduate_work/data/news/" +datetime.datetime.now().strftime("%B")+"/"+ time.strftime("%d/%m/%Y").replace('/', '_') + ".xml", "w") as text_file:
    print(handle, file=text_file)
