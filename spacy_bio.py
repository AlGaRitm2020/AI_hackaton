import spacy


def add_labels(ent, name):
    label = []
    for i in range(len(str(ent).split())):
        if i == 0:
            label.append(f'B-{name}')
        else:
            label.append(f'I-{name}')
    print(label)
    return label


def get_labels(text):
    nlp = spacy.load("ru_core_news_md")
    doc = nlp(text)
    # print(doc.text)
    splited = text.split()
    labels = []
    ch = [str(i) for i in range(1, 32)] + [str(i) for i in range(1500, 2500)]
    date = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
            'декабрь', 'января', 'январю', 'январем', 'февраля', 'февралю', 'февралем', 'марта', 'марту', 'мартом',
            'апреля', 'апрелю', 'апрелем', 'мая', 'маю', 'маем', 'июня', 'июню', 'июнем', 'июля', 'июлем', 'июлю',
            'августа', 'августу', 'августом', 'сентября', 'сентябрю', 'сентябрем', 'октября', 'октябрю', 'октябрем',
            'ноября', 'ноябрю', 'ноябрем', 'декабря', 'декабрю', 'декабрем']
    last = doc.ents[3]
    for ent in doc.ents:
        for i, elem in enumerate(text.split()):
            flag = 0
            if elem not in str(ent):

                if text.split()[i] in date and not flag:

                    if text.split()[i - 1] in ch:
                        if text.split()[i + 1] in ch:

                            labels.append('B-DATE')
                            labels.append('I-DATE')
                            labels.append('I-DATE')
                            # print(text.split()[i - 1], text.split()[i], text.split()[i + 1], ': DATE')
                        else:
                            labels.append('B-DATE')
                            labels.append('I-DATE')
                            # print(text.split()[i - 1], text.split()[i], ': DATE')
                    elif text.split()[i + 1] in ch:
                        labels.append('B-DATE')
                        labels.append('I-DATE')
                        # print(text.split()[i], text.split()[i + 1], ': DATE')
                    else:
                        labels.append('B-DATE')

                        # print(text.split()[i], ': DATE')
                else:

                    labels.append('0')
                    continue
            elif not last == ent:
                last = ent

                if ent.label_ == 'ORG':
                    labels += add_labels(ent, "ORGANIZATION")
                if ent.label_ == 'LOC':
                    print(ent, elem)
                    labels += add_labels(ent, "LOCATION")
                if ent.label_ == 'PER':
                    labels += add_labels(ent, "PERSON")
            else:
                continue
    #
    #
    # for i in range(len(text.split())):
    #     if text.split()[i] in date:
    #         if text.split()[i - 1] in ch:
    #             if text.split()[i + 1] in ch:
    #                 pass
    #                 # print(text.split()[i - 1], text.split()[i], text.split()[i + 1], ': DATE')
    #             else:
    #                 pass
    #                 # print(text.split()[i - 1], text.split()[i], ': DATE')
    #         elif text.split()[i + 1] in ch:
    #             pass
    #             # print(text.split()[i], text.split()[i + 1], ': DATE')
    #         else:
    #             pass
    #             # print(text.split()[i], ': DATE')
    for i in range(len(text.split())):
        if i in ch:
            pass
    for i in range(len(text.split())):
        print(splited[i], labels[i])
    print(labels)


if __name__ == '__main__':
    text = 'Еду в Санкт-Петербург Яндекс через Москву, Алексей 12 августа года Ижевску ООО "Яндекс" 10000$ Кононов Никита Владимирович мама папа Китай Пекин МТС и директор Абу-Даби Хельсинки'
    get_labels(text)