from flask import Flask, Blueprint, render_template, request, send_file, redirect, url_for
import os
from test_json import check_values


app = Flask(__name__)
check_empty_values = Blueprint('check-values', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@check_empty_values.route('/check-values', methods=['POST', 'GET'])
def check_keys_1():
    name = ""
    visibility = 'hidden'
    if name == 'Json filename(filepath) is incorrect':
        visibility = 'visible'
    return render_template("check_values.html", visibility=visibility, name=name)


@check_empty_values.route('/down-vals', methods=['POST', 'GET'])
def check_vals_1():
    global name
    name = ""
    visibility = 'hidden'
    if request.method == 'POST':
        file = request.files['file']
        if file:
            visibility = 'visible'
            filename = file.filename
            if filename.split('.')[-1] != 'json':
                return redirect(url_for("check-values.check_keys_1", name=name))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            name = check_values(file_path)
    if name == 'Json filename(filepath) is incorrect':
        visibility = 'hidden'
    return redirect(url_for("check-values.downloadFile_5", name=name))


@check_empty_values.route('/k_download')
def downloadFile_5 ():
    path = name
    return send_file(path, as_attachment=True)
#'<video width="320" height="240" controls src="">','<img src="https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_1GAUXXH6KZR4Y.jpeg" alt="an artists rendition of a black hole in space" width="300px" height="300px">' , '<img src="https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_RJF1ZJQBJ60OS.jpeg" alt="an artists rendition of a black hole in space" width="300px" height="300px">','<img src="https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_RZ29BL791P5I9.jpeg" alt="an artists rendition of a black hole in space" width="300px" height="300px">','<img src="https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_RZ29BL791P5I9.jpeg" alt="an artists rendition of a black hole in space" width="300px" height="300px">','<img src="https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_RZ29BL791P5I9.jpeg" alt="an artists rendition of a black hole in space" width="300px" height="300px">'