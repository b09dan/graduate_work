#  Some helpful tips for parsing: https://gist.github.com/b09dan/99f79a35e87d426bcc720e71b45b2899
def xml_2_array(xml_name):
    from lxml import etree

    # tree = etree.XML(news_xml) # String parsing
    news_xml = etree.parse(xml_name)  # File parsing
    nodes = news_xml.xpath('/parsed/news_for_today/article ')  # opening a section
    news_xml_array = []  # Creating an empty array for articles
    for node in nodes:  # Sorting out each tag
        news_xml_array.append(
            str([node.text]).replace('[', '').replace(']', '').split(', '))  # Taking a list, converting to string
        #  and removing [ ] symbols
    for i in range(0, len(news_xml_array)):
        for j in range(0, len(news_xml_array[i])):
            news_xml_array[i][j] = news_xml_array[i][j].replace("'", "")  # Removing quotes
            # at the start and at the end of each article
    return news_xml_array
