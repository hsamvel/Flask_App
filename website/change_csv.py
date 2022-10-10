from flask import Flask, Blueprint, render_template, request, send_file, redirect, url_for
import os
from csv_changer import change_csv_1


app = Flask(__name__)
change_csv = Blueprint('change_csv', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@change_csv.route('/change-csv', methods=['POST', 'GET'])
def login_1():
    name = ""
    return render_template("change_csv.html")


@change_csv.route('/down-change-csv', methods=['POST', 'GET'])
def login():
    file = ''
    global name
    name = ""
    if request.method == 'POST':
        text = request.form['name']
        if not text:
            text = "No link specified"
        file = request.files['file']
        if not file:
            return render_template("change_csv.html")
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        name = change_csv_1(file_path, text)
        print(name)
    return redirect(url_for("change_csv.downloadFile_3", name=name))


@change_csv.route('/download_csv')
def downloadFile_3 ():
    path = name
    return send_file(path, as_attachment=True)