from flask import Flask, Blueprint, render_template, request, send_file, redirect, url_for
import os
from test_json import check_syntax


app = Flask(__name__)
check_syntax_ = Blueprint('check-syntax', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@check_syntax_.route('/check-syntax', methods=['POST', 'GET'])
def check_syntax_1():
    name = ""
    visibility = 'hidden'
    return render_template("check_syntax.html", visibility=visibility, name=name)


@check_syntax_.route('/down-syntax', methods=['POST', 'GET'])
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
                return redirect(url_for("check-syntax.check_syntax_1", name=name))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            name = check_syntax(file_path)
    if name == 'Json filename(filepath) is incorrect':
        visibility = 'hidden'
    return redirect(url_for("check-syntax.downloadFile_11", name=name))


@check_syntax_.route('/sh1_download')
def downloadFile_11 ():
    path = name
    return send_file(path, as_attachment=True)
