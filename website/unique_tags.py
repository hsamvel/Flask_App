from flask import Flask, Blueprint, render_template, request, send_file, redirect, url_for
import os
from test_json import check_unique_tags


app = Flask(__name__)
unique_tags = Blueprint('unique-tags', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@unique_tags.route('/unique-tags', methods=['POST', 'GET'])
def check_keys_2():
    name = ""
    visibility = 'hidden'
    return render_template("unique_tags.html", visibility=visibility, name=name)


@unique_tags.route('/down-un-tags', methods=['POST', 'GET'])
def check_keys_1():
    global name
    name = ""
    visibility = 'hidden'
    if request.method == 'POST':
        file = request.files['file']
        visibility = 'visible'
        if file:
            filename = file.filename
            if filename.split('.')[-1] != 'json':
                return redirect(url_for("unique-tags.check_keys_2", name=name))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            name = check_unique_tags(file_path)
    if name == 'Json filename(filepath) is incorrect':
        visibility = 'hidden'
    return redirect(url_for("unique-tags.downloadFile_12", name=name))


@unique_tags.route('/sh3_download')
def downloadFile_12 ():
    path = name
    return send_file(path, as_attachment=True)
