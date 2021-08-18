import pytesseract
from PIL import Image
import json

def func_for_vision_words_with_coord(img): # функция для обработкии изображения
    # импорт библиотеки
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # открытие изображения
    image = Image.open(img)

    # обработка текста на русском языке
    text_from_vision = rus_func(img)
    # информация о каждом слове и его характеристики
    text_data = pytesseract.image_to_data(img, lang='rus')

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
                    'offset': text_from_vision.find(list_elems[-1])

                }
                dict['tokens'].append(dict_tokens)
    # запись в json файл

    with open('data_1.json', 'w') as f:
        json.dump(dict, f)



def img_size(img): # размер изображения
    im = Image.open(img)
    return im.size

def rus_func(img): # функция для обработки русского языка
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(img, lang="rus")
    with open('text_from_image3.txt', 'a', encoding='utf-8') as f:
        f.write(text.strip())

    with open('text_from_image3.txt', encoding='utf-8') as f:
        f = f.read()
        mass = []
        for i in f.split('\n'):
            if i not in ['  ', ' ', '']:
                mass.append(i)
        return ' '.join(mass)

if __name__ == '__main__':
    func_for_vision_words_with_coord('aah97e00-page02_1.tif')

