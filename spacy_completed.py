import spacy

from NLP import check_stems, get_stems
from keywords import KeyWords


def add_loc_org_and_person(ent, name):
    dict = {}
    dict['text'] = ent.text
    dict['tag'] = name
    dict['tokens'] = []
    offset = 0
    for elem in ent.text.split():
        token = {
            'text': elem,
            'offset': offset
        }
        offset += len(elem) + 1
        dict['tokens'].append(token)
    return dict


def add_date_or_money(*data, name='DATE'):
    dict = {}
    dict['text'] = ' '.join(data)
    dict['tag'] = name
    dict['tokens'] = []
    offset = 0
    for elem in data:
        token = {
            'text': elem,
            'offset': offset
        }
        offset += len(elem) + 1
        dict['tokens'].append(token)
    return dict


def get_labels_dict(text):
    nlp = spacy.load("ru_core_news_sm")
    doc = nlp(text)

    response = {'facts': []}
    for ent in doc.ents:
        if ent.label_ == 'ORG':
            response['facts'].append(add_loc_org_and_person(ent, 'ORGANIZATION'))
        if ent.label_ == 'LOC':
            response['facts'].append(add_loc_org_and_person(ent, 'LOCATION'))
        if ent.label_ == 'PER':
            response['facts'].append(add_loc_org_and_person(ent, 'PERSON'))

    ch = ['0' + str(i) for i in range(1, 10)]
    ch += [str(i) for i in range(1, 32)]
    ch += [str(i) for i in range(1500, 2050)]

    for i in range(len(text.split()) - 1):
        if check_stems(get_stems(text.split()[i]), KeyWords.months):

            if text.split()[i - 1] in ch:
                if text.split()[i + 1] in ch:
                    dict = add_date_or_money(text.split()[i - 1], text.split()[i],
                                             text.split()[i + 1])
                    response['facts'].append(dict)

                else:

                    dict = add_date_or_money(text.split()[i - 1], text.split()[i])
                    response['facts'].append(dict)
            elif text.split()[i + 1] in ch:

                dict = add_date_or_money(text.split()[i], text.split()[i + 1])
                response['facts'].append(dict)
            else:
                dict = add_date_or_money(text.split()[i])
                response['facts'].append(dict)

    for i in range(len(text.split()) - 1):
        if text.split()[i] in ch:
            if check_stems(get_stems(text.split()[i + 1]), KeyWords.years):
                dict = add_date_or_money(text.split()[i], text.split()[i + 1])
                response['facts'].append(dict)
    for i in range(len(text.split())):
        if str(text.split()[i][:-1:]) in ch:
            if text.split()[i][-1] == 'г':
                dict = add_date_or_money(text.split()[i])
                response['facts'].append(dict)
        if str(text.split()[i][:-2:]) in ch:
            if text.split()[i][-2::] == 'г.':
                dict = add_date_or_money(text.split()[i])
                response['facts'].append(dict)

    for i in range(len(text.split())):
        flag = 0
        if len(text.split()[i]) > 3:
            if (text.split()[i]).count('.') == 3:
                if str(text.split()[i][-1]) == '.':
                    flag = 1
            if flag == 1:
                if str(text.split()[i])[-2] == 'г':
                    if str(text.split()[i].split('.')[0]) in ch and str(
                            text.split()[i].split('.')[1]) in ch:
                        dict = add_date_or_money(text.split()[i][:-1])
                        response['facts'].append(dict)
                else:
                    if str(text.split()[i].split('.')[0]) in ch and str(
                            text.split()[i].split('.')[1]) in ch:
                        dict = add_date_or_money(text.split()[i])
                        response['facts'].append(dict)
            if (text.split()[i]).count('.') == 2:
                if str(text.split()[i][-1]) == 'г':
                    if str(text.split()[i].split('.')[0]) in ch and str(
                            text.split()[i].split('.')[1]) in ch:
                        dict = add_date_or_money(text.split()[i])
                        response['facts'].append(dict)
                else:
                    if str(text.split()[i].split('.')[0]) in ch and str(
                            text.split()[i].split('.')[1]) in ch:
                        dict = add_date_or_money(text.split()[i])
                        response['facts'].append(dict)

    for i in range(len(text.split()) - 1):
        if (text.split()[i]).isdigit():
            if check_stems(get_stems(text.split()[i + 1]), KeyWords.money):
                dict = add_date_or_money(text.split()[i], text.split()[i + 1], name='MONEY')
                response['facts'].append(dict)

    return response


if __name__ == '__main__':
    text = 'Еду в Санкт-Петербург Яндекс через 1892г 2010г. 1900 г Москву, 1004678765 рублей 13.05.2003г. Алексей 12 августа года Ижевску ООО "Яндекс" 10000$ 1734г Кононов Никита Владимирович мама папа Китай Пекин МТС и директор Абу-Даби Хельсинки'
    # print(get_labels_dict(text))
