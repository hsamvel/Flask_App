from flask import Flask, Blueprint, render_template, request, send_file, redirect, url_for,session,json
import os
from jsot_to_csv import json_csv_conv


app = Flask(__name__)
json_csv = Blueprint('json-csv', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@json_csv.route('/csv-json', methods=['POST', 'GET'])
def login():
    return render_template("json_to_csv.html")


@json_csv.route('/new-page_11', methods=['POST', 'GET'])
def new_fn():
    name = ''
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        if filename.split('.')[-1] != 'json':
            return redirect(url_for("json-csv.login"))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        visibility = 'visible'
        name = json_csv_conv(file_path)
        json.dumps({"main": name})
        session['name'] = name
        print(name)
        msg = 'Scroll down to download converted file'
    return redirect(url_for("json-csv.downloadFile123", name=name))


@json_csv.route('/download12')
def downloadFile123 ():
    name = session['name']
    return send_file(name, as_attachment=True)
