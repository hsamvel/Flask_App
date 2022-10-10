from flask import Flask, Blueprint, render_template, request, send_file,redirect,url_for
import os
from test_json import check_keys


app = Flask(__name__)
check_empty_keys = Blueprint('check-keys', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@check_empty_keys.route('/check-keys', methods=['POST', 'GET'])
def check_keys_1():
    name = ""
    visibility = 'hidden'
    if name == 'Json filename(filepath) is incorrect' or not name:
        visibility = 'hidden'
    return render_template("check_keys.html", visibility=visibility, name=name)


@check_empty_keys.route('/down-keys', methods=['POST', 'GET'])
def check_keys_2():
    global name
    name = ""
    visibility = 'hidden'
    if request.method == 'POST':
        file = request.files['file']
        if file:
            visibility = 'visible'
            filename = file.filename
            if filename.split('.')[-1] != 'json':
                return redirect(url_for("check-keys.check_keys_1", name=name))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            name = check_keys(file_path)
    if name == 'Json filename(filepath) is incorrect':
        visibility = 'hidden'
    return redirect(url_for("check-keys.downloadFile_5", name=name))

@check_empty_keys.route('/z_download')
def downloadFile_5 ():
    path = name
    return send_file(path, as_attachment=True)
