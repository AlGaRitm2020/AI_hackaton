import spacy
# def add_facts(ent, )
texty = 'Еду в Санкт-Петербург Яндекс через 1892г 2010г. 1900 г Москву, 1004678765 рублей 13.05.2003г. Алексей 12 августа года Ижевску ООО "Яндекс" 10000$ 1734г Кононов Никита Владимирович мама папа Китай Пекин МТС и директор Абу-Даби Хельсинки'
nlp = spacy.load("ru_core_news_sm")
doc = nlp(texty)
print(doc.text)
response = {'facts': None}
for ent in doc.ents:
    if ent.label_ == 'ORG':
        dict = {}
        dict['text'] = ent.text
        dict['tag'] = 'ORGANIZATION'
        dict['tokens'] = []
        offset = 0
        for elem in ent.text.split():
            token = {
                'text' : elem,
                'offset' : offset
            }
            offset += len(elem) + 1
            dict['tokens'].append(token)
        print(ent.text, ': ORGANIZATION')
    if ent.label_ == 'LOC':
        dict = {}
        dict['text'] = ent.text
        dict['tag'] = 'LOCATION'
        print(ent.text, ': LOCATION')
    if ent.label_ == 'PER':
        dict = {}
        dict['text'] = ent.text
        dict['tag'] = 'PERSON'
        print(ent.text, ': PERSON')

ch = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
for i in range(1, 32):
    ch.append(i)

for i in range(1500, 2050):
    ch.append(i)
ch = [str(i) for i in ch]
date = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь', 'января', 'январю', 'январем', 'февраля', 'февралю', 'февралем', 'марта', 'марту', 'мартом', 'апреля', 'апрелю', 'апрелем', 'мая', 'маю', 'маем', 'июня', 'июню', 'июнем', 'июля', 'июлем', 'июлю', 'августа', 'августу', 'августом', 'сентября', 'сентябрю', 'сентябрем', 'октября', 'октябрю', 'октябрем', 'ноября', 'ноябрю', 'ноябрем', 'декабря', 'декабрю', 'декабрем']
for i in range(len(texty.split())):
    if texty.split()[i] in date:
        if texty.split()[i - 1] in ch:
            if texty.split()[i + 1] in ch:
                print(texty.split()[i - 1], texty.split()[i], texty.split()[i + 1], ': DATE')
            else:
                print(texty.split()[i - 1], texty.split()[i], ': DATE')
        elif texty.split()[i + 1] in ch:
            print(texty.split()[i], texty.split()[i + 1], ': DATE')
        else:
            print(texty.split()[i], ': DATE')
for i in range(len(texty.split())):
    if texty.split()[i] in ch:
        if texty.split()[i + 1] in ['г.', 'год', 'года', 'году', 'г', 'год.', 'года.', 'году.']:
            print(texty.split()[i], texty.split()[i + 1], ': DATE',)
for i in range(len(texty.split())):
    if str(texty.split()[i][:-1:]) in ch:
        if texty.split()[i][-1] == 'г':
            print(texty.split()[i], ': DATE')
    if str(texty.split()[i][:-2:]) in ch:
        if texty.split()[i][-2::] == 'г.':
            print(texty.split()[i], ': DATE')
flag = 0
for i in range(len(texty.split())):
    flag = 0
    if len(texty.split()[i]) > 3:
        if (texty.split()[i]).count('.') == 3:
            if str(texty.split()[i][-1]) == '.':
                flag = 1
        if flag == 1:
            if str(texty.split()[i])[-2] == 'г':
                if str(texty.split()[i].split('.')[0]) in ch and str(texty.split()[i].split('.')[1]) in ch:
                    print(texty.split()[i][:-1], ': DATE')
            else:
                if str(texty.split()[i].split('.')[0]) in ch and str(texty.split()[i].split('.')[1]) in ch:
                    print(texty.split()[i], ': DATE')
        if (texty.split()[i]).count('.') == 2:
            if str(texty.split()[i][-1]) == 'г':
                if str(texty.split()[i].split('.')[0]) in ch and str(texty.split()[i].split('.')[1]) in ch:
                    print(texty.split()[i], ': DATE')
            else:
                if str(texty.split()[i].split('.')[0]) in ch and str(texty.split()[i].split('.')[1]) in ch:
                    print(texty.split()[i], ': DATE')

for i in range(len(texty.split())):
    if (texty.split()[i]).isdigit():
        if str(texty.split()[i + 1]) in ['рублей', 'руб.', 'руб', 'рублей.', 'долларов', '$', 'р.', 'р', 'евро', 'евро.']:
            print(texty.split()[i], texty.split()[i + 1], ': MONEY')