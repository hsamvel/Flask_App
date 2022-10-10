from flask import Flask, Blueprint, render_template, request, send_file, redirect, url_for
import os
from csv_json_generator import generate_json
from check_links import check_link
from test_json import check_animation_urls
from test_json import check_image_urls


app = Flask(__name__)
gen_json = Blueprint('gen_json', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@gen_json.route('/gen-json', methods=['POST', 'GET'])
def login():
    return render_template("gen_json.html")


@gen_json.route('/new-page', methods=['POST', 'GET'])
def new_fn():
    msg = ''
    visibility = 'hidden'
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            if filename.split('.')[-1] != 'csv':
                return redirect(url_for("gen_json.login"))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            visibility = 'visible'
            global name
            name = generate_json(file_path)
            msg = 'Scroll down to download converted file'
            if name == 'Csv filename(filepath) is incorrect':
                msg = 'Csv filename(filepath) is incorrect'
                visibility = 'hidden'
    return redirect(url_for("gen_json.downloadFile", name=name))


@gen_json.route('/download')
def downloadFile ():
    path = name
    return send_file(path, as_attachment=True)
