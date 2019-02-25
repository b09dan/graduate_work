# from nltk.tokenize import sent_tokenize, word_tokenize
#
# EXAMPLE_TEXT = "Проделав такую работу для всех отзывов мы можем получить достаточно большой список (в моем примере я взял 5000 самые часто встречающие слова). Эти вектора называются «векторами свойств» или же «features vector». Таким образом мы получаем вектора для каждого тестового отзыва, дальше мы сможем сравнивать эти вектора с помощью стандартных метрик, таких как Евклидовое расстояние, косинусное расстояние, и т.д. Данный подход называется «мешок слов» или же “Bag-Of-Words”."
# print(word_tokenize(EXAMPLE_TEXT))

import nltk
from nltk.stem.porter import PorterStemmer #Loading library fo stemming words

def get_tokens():
    with open('stem_sample.txt') as stem:
        tokens = nltk.word_tokenize(stem.read())
    return tokens


def do_stemming(filtered):
    stemmed = []
    for f in filtered:
        stemmed.append(PorterStemmer().stem(f))
    return stemmed


if __name__ == "__main__":
    tokens = get_tokens()
    print(tokens)

    stemmed_tokens = do_stemming(tokens)
    print(stemmed_tokens)

    result = dict(zip(tokens, stemmed_tokens))
    print(result)
