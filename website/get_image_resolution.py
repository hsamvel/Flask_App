from flask import Flask, Blueprint, render_template, request, send_file
import os
from test_json import get_image_link


app = Flask(__name__)
image_resolution = Blueprint('image-res', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@image_resolution.route('/image-res', methods=['POST', 'GET'])
def check_keys_1():
    name = ""
    visibility = 'hidden'
    if request.method == 'POST':
        file = request.files['file']
        visibility = 'visible'
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            name = get_image_link(file_path)
    if name == 'Json filename(filepath) is incorrect':
        visibility = 'hidden'
    return render_template("image_resolution.html", visibility=visibility, name=name)


@image_resolution.route('/sh4_download')
def downloadFile_12 ():
    path = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\image_resolution_check_results.txt'
    return send_file(path, as_attachment=True)
