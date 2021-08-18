from keywords import KeyWords
from spacy_completed import get_labels_dict


def is_main(text):
    splited = text.lower().split()

    for key in KeyWords.pages:
        if key in splited:
            try:
                if int(splited[splited.index(key) + 1]) > 1:
                    return 'other'
                elif int(splited[splited.index(key) + 1]) == 1:
                    return 'main'
            except ValueError:
                pass

    labels_set = set([fact['tag'] for fact in get_labels_dict(text)['facts']])

    print(labels_set)
    if KeyWords.compulsory_labels <= labels_set:
        return 'main'
    else:
        return 'other'


if __name__ == '__main__':
    text = 'Еду в Санкт-Петербург Яндекс через 1892г 2010г. 1900 г Москву, 1004678765 рублей 13.05.2003г. Алексей 12 августа года Ижевску  10000$ 1734г Кононов Никита Владимирович мама'
    print(is_main(text))
