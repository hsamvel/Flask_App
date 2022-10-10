from flask import Flask, Blueprint, render_template, request, send_file, redirect, url_for
import os
from test_json import calculate_arguments


app = Flask(__name__)
calc_args = Blueprint('calculate-arguments', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@calc_args.route('/calculate-arguments', methods=['POST', 'GET'])
def check_keys_1():
    visibility = 'hidden'
    name = ''
    if name == 'Json filename(filepath) is incorrect':
        visibility = 'hidden'
    return render_template("calculate_args.html", visibility=visibility, name=name)


@calc_args.route('/down-calcs', methods=['POST', 'GET'])
def calc_args_1():
    global name
    name = ''
    if request.method == 'POST':
        file = request.files['file']
        visibility = 'visible'
        if file:
            filename = file.filename
            if filename.split('.')[-1] != 'json':
                return redirect(url_for("calculate-arguments.check_keys_1"))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            name = calculate_arguments(file_path)
    if name == 'Json filename(filepath) is incorrect':
        visibility = 'hidden'
    return redirect(url_for("calculate-arguments.downloadFile_9", name=name))


@calc_args.route('/sh_download')
def downloadFile_9 ():
    path = name
    return send_file(path, as_attachment=True)
