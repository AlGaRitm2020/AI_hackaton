import pytesseract
from PIL import Image


def func_for_vision_words_with_coord(img):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text_data = pytesseract.image_to_data(Image.open(img))

    image = Image.open(img)

    text_from_vision = pytesseract.image_to_string(image, lang="eng").strip()
    text_from_vision_with_enter = text_from_vision.replace('\n\n', '\n')
    text_from_vision = text_from_vision.replace('\n', ' ')


    dict = {
        'text': text_from_vision,
        'tokens': [],
        'source':{
            'width': img_size(img)[0],
            'height':img_size(img)[1]
        }
    }


    for i, s in enumerate(text_data.split('\n')[1:]):
        list_elems = s.split('\t')
        # предложения - отдельно
        elems_text_from_vision = text_from_vision_with_enter.split('\n')

        # offset = 0
        #
        # for number_string, string in reversed(list(enumerate(elems_text_from_vision))):
        #     if list_elems[-1] in string:
        #         offset = string
        #         del elems_text_from_vision[number_string]






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
                    'offset': [j for j in elems_text_from_vision if list_elems[-1] in j][0].find(list_elems[-1])

                }
                dict['tokens'].append(dict_tokens)





    import json
    with open('data_1.json', 'w') as f:
        json.dump(dict, f)


def main_page(name_file):
    if '_' in name_file.split('/')[-1]:
        list_name_file = name_file.split('_')
        number = list_name_file[-1].split('.')[0]
        if number == '1':
            return True
        return False
    return True


def img_size(img):
    from PIL import Image
    im = Image.open(img)
    (width, height) = im.size
    return (width, height)


# func_for_vision_words_with_coord('source/aah97e00-page02_1.tif')
#
# print(img_size('source/aah97e00-page02_1.tif'))