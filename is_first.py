def is_main(text):
    splited = text.split()
    if 'стр' in splited or 'страница' in splited:
        try:

            if int(splited[splited.index('стр') + 1]) > 1:
                return 'other'
            elif int(splited[splited.index('страница') + 1]) > 1:
                return 'other'
            else:
                return 'main'
        except ValueError:
            pass
    return 'main'


if __name__ == '__main__':
    text = 'страница 5'
    print(is_main(text))