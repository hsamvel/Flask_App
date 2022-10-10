from flask import Flask, Blueprint, render_template, request, send_file, redirect, url_for
import os
from test_json import check_unique_links


app = Flask(__name__)
unique_links = Blueprint('unique-links', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@unique_links.route('/unique-links', methods=['POST', 'GET'])
def check_keys_2():
    name = ""
    visibility = 'hidden'
    return render_template("unique_links.html", visibility=visibility, name=name)


@unique_links.route('/down-un-links', methods=['POST', 'GET'])
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
                return redirect(url_for("unique-links.check_keys_2", name=name))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            name = check_unique_links(file_path)
    if name == 'Json filename(filepath) is incorrect':
        visibility = 'hidden'
    return redirect(url_for("unique-links.downloadFile_9", name=name))


@unique_links.route('/sh2_download')
def downloadFile_9 ():
    path = name
    return send_file(path, as_attachment=True)
