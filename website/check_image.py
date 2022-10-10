from flask import Flask, Blueprint, render_template, request, send_file, redirect, url_for
import os
from csv_json_generator import generate_json
from check_links import check_link
from test_json import check_animation_urls
from test_json import check_image_urls


app = Flask(__name__)
check_image = Blueprint('check-image', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@check_image.route('/check-image', methods=['POST', 'GET'])
def check_image_urls_1():
    name = ""
    visibility = 'hidden'
    return render_template("check_image.html", visibility=visibility, name=name)


@check_image.route('/down-image', methods=['POST', 'GET'])
def check_image_urls_2():
    global name
    name = ""
    visibility = 'hidden'
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            if filename.split('.')[-1] != 'json':
                return redirect(url_for("check-image.check_image_urls_1"))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            name = check_image_urls(file_path)
            visibility = 'visible'
    if name == 'Json filename(filepath) is incorrect':
        visibility = 'hidden'
    return redirect(url_for("check-image.downloadFile_3", name=name))


@check_image.route('/c_download')
def downloadFile_3():
    path = name
    return send_file(path, as_attachment=True)
