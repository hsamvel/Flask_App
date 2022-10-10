from flask import Flask, Blueprint, render_template, request, send_file, redirect ,url_for
import os
from test_json import check_tag_domain_last_digits


app = Flask(__name__)
check_tag_with_domain = Blueprint('check-tag-domain', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@check_tag_with_domain.route('/check-tag-domain', methods=['POST', 'GET'])
def check_keys_2():
    name = ""
    visibility = 'hidden'
    return render_template("check_tag_with_domain.html", visibility=visibility, name=name)


@check_tag_with_domain.route('/down-tag-domain', methods=['POST', 'GET'])
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
                return redirect(url_for("check-tag-domain.check_keys_2", name=name))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            name = check_tag_domain_last_digits(file_path)
    if name == 'Json filename(filepath) is incorrect':
        visibility = 'hidden'
    return redirect(url_for("check-tag-domain.downloadFile_7", name=name))


@check_tag_with_domain.route('/u_download')
def downloadFile_7 ():
    path = name
    return send_file(path, as_attachment=True)
