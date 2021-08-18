import pytesseract
from PIL import Image
import json

def func_for_vision_words_with_coord(img): # функция для обработкии изображения
    # импорт библиотеки
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # открытие изображения
    image = Image.open(img)

    # распознание текста на изображении и удаление \n и \n\n
    text_from_vision = pytesseract.image_to_string(image, lang="eng").strip()
    text_from_vision = text_from_vision.replace('\n\n', '\n')
    text_from_vision_with_enter = text_from_vision.replace('\n\n', '\n')
    text_from_vision = text_from_vision.replace('\n', ' ')
    # информация о каждом слове и его характеристики
    text_data = pytesseract.image_to_data(img)

    # начальный словарь
    dict = {
        'text': text_from_vision,
        'tokens': [],
        'source':{
            'width': img_size(img)[0],
            'height':img_size(img)[1]
        }
    }


    text_full = []
    # анализ каждого слова в тексте
    for i, s in enumerate(text_data.split('\n')[1:]):
        list_elems = s.split('\t')
        text_full.append(list_elems[-1])
        # отдельный строчки текста
        elems_text_from_vision = text_from_vision_with_enter.split('\n')

        # если все характеристики слова существуют
        if len(list_elems) == 12:
            if list_elems[-1] != '' and list_elems[-1] != ' ':
                # наполнение списка tokens для кадого слова
                dict_tokens = {
                    'text': list_elems[-1],
                    'position': {
                        'left': list_elems[6],
                        'top': list_elems[7],
                        'width': list_elems[8],
                        'height': list_elems[9]
                    },
                    'offset': [j for j in elems_text_from_vision if list_elems[-1] in j][0].find(list_elems[-1])

                }
                dict['tokens'].append(dict_tokens)
    # запись в json файл

    with open('data_1.json', 'w') as f:
        json.dump(dict, f)


def img_size(img): # размер изображения
    im = Image.open(img)
    return im.size



