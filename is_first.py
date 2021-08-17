def is_first(text):
    splited = text.split()
    if 'page' in splited:
        if int(splited[splited.index('page') + 1]) > 1:
            return False
    return True


if __name__ == '__main__':
    text = 'page '
    print(is_first(text))