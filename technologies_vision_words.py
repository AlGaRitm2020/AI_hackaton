import pytesseract
from PIL import Image


def func_for_vision_words_with_coord(img):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_data(Image.open(img))


    image = Image.open(img)


    text_from_vision = pytesseract.image_to_string(image, lang="eng").strip()


    dict = {
        'text': text_from_vision,
        'tokens': []
    }
    for i, s in enumerate(text.split('\n')[1:]):
        list_elems = s.split('\t')
        if len(list_elems) == 12:
            if list_elems[-1] != '' and list_elems[-1] != ' ':

                dict_tokens = {
                    'text': list_elems[-1],
                    'position': {
                        'left': list_elems[6],
                        'top': list_elems[7],
                        'width': list_elems[8],
                        'height': list_elems[9]
                    },
                    'offset': None

                }
                dict['tokens'].append(dict_tokens)





    import json
    with open('data.json', 'w') as f:
        json.dump(dict, f)


func_for_vision_words_with_coord('source/aah97e00-page02_1.tif')
