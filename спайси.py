import spacy

texty = 'Еду в Санкт-Петербург Яндекс через Москву, Алексей 12 августа года Ижевску ООО "Яндекс" 10000$ Кононов Никита Владимирович мама папа Китай Пекин МТС и директор Абу-Даби Хельсинки'
nlp = spacy.load("ru_core_news_sm")
doc = nlp(texty)
print(doc.text)
for ent in doc.ents:
    if ent.label_ == 'ORG':
        print(ent.text, ': ORGANIZATION', sep='')
    if ent.label_ == 'LOC':
        print(ent.text, ': LOCATION', sep='')
    if ent.label_ == 'PER':
        print(ent.text, ': PERSON', sep='')

ch = []
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
    if i in ch:
        pass
