import os
from flask import Flask, request, render_template

UPLOAD_FOLDER = './upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def render_templatete(param):
    pass


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'img' not in request.files:
            return 'there is no file1 in form!'
        img = request.files['img']
        path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(path)

        text = 'get from function by snchs'
        dict = {'text': text}

        # import json
        # with open('text.json', 'w') as f:
        #     json.dump(dict, f)
        return dict, 201
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()