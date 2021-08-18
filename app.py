import json
import os
import uuid

from flask import Flask, request, render_template

from img_to_text import img_to_text
from is_first import is_main
from technologies_vision_words import func_for_vision_words_with_coord, img_size
from spacy_completed import get_labels_dict

UPLOAD_FOLDER = './upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/text_extraction', methods=['GET', 'POST'])
def text_extraction():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'

        img = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(path)

        func_for_vision_words_with_coord(os.path.join(path))

        # import json
        with open('data.json', 'r') as f:
            return json.load(f), 201

    return render_template('1_text_extraction.html')


@app.route('/search_logo', methods=['GET', 'POST'])
def search_logo():
    if request.method == 'POST':
        if 'img' not in request.files:
            return 'there is no file1 in form!'
        images = request.files.getlist("pictures")
        if images:
            for img in images:
                # Create Images
                file_name = img.filename
                image_file = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
                img.save(image_file)

        img = request.files['img']
        path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(path)

        text = 'get from function by snchs'
        dict = {'text': text}

        # import json
        # with open('text.json', 'w') as f:
        #     json.dump(dict, f)
        return dict, 201
    return render_template('2_search_logo.html')


@app.route('/classification', methods=['GET', 'POST'])
def classification():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        img = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(path)

        text = img_to_text(path)
        width, height = img_size(path)
        dict = {'width': width,
                'height': height,
                'type': is_main(text)}

        return dict, 201
    return render_template('3_classification.html')


@app.route('/get_labels', methods=['GET', 'POST'])
def get_labels():
    if request.method == 'POST':
        text = request.form.get('text1')
        response = get_labels_dict(text)

        return f"""Response: {response}""", 201
    return render_template('4_get_labels.html')


if __name__ == '__main__':
    app.run()
