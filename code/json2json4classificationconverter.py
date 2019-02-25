import json


with open('/home/bogdan/PycharmProjects/graduate_work/data/fox_business/20_04_2017_02_07.json') as data_file:
    data = json.load(data_file)

all_articles = []
for article in data.get('articles_data'):
    temp_arr_4_classes= [article.get('theme')]
    array_article = {
            'classes': temp_arr_4_classes,
            'text': article.get('source_text')
            }
    all_articles.append(array_article)
with open("/home/bogdan/PycharmProjects/graduate_work/data/fox_business/ready_4_classification.json", "w") as text_file:
    print(
        json.dumps(
            all_articles,
            indent=4,
            sort_keys=True
        )
    , file=text_file)