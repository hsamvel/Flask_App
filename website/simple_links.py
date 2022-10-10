from flask import Flask, Blueprint, render_template, request, send_file
import os
from csv_json_generator import generate_json
from check_links import check_link
from test_json import check_animation_urls
from test_json import check_image_urls


app = Flask(__name__)
simple_link = Blueprint('simple_links', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')
name = ''


# @auth.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             filename = file.filename
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             print(file)
#             file.save(file_path)
#             print(file_path)
#             #global name
#             generate_json(file_path)
#             #print(name)
#     return render_template("gen_json.html", name='Cool!')
#
#
# @auth.route('/download')
# def downloadFile ():
#     path = "your_json_from_csv.json"
#     return send_file(path, as_attachment=True)


@simple_link.route('/check-simple-links', methods=['POST', 'GET'])
def signup():
    visibility = 'hidden'
    visibility_1 = 'hidden'
    visibility_2 = 'hidden'
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            check_link(file_path)
            visibility = 'visible'
    return render_template("simple_links.html", visibility=visibility, visibility_1=visibility_1, visibility_2=visibility_2)


# @auth.route('/sign-up-again', methods=['POST', 'GET'])
# def signupagain():
#     visibility_1 = 'hidden'
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             filename = file.filename
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(file_path)
#             name = check_animation_urls(file_path)
#             visibility_1 = 'visible'
#             if name:
#                 message = name
#             else:
#                 message = 'Checking'
#     return render_template("sign_up.html", visibility=visibility_1)


# @auth.route('/sign-up-more', methods=['POST', 'GET'])
# def signupmore():
#     visibility_2 = 'hidden'
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             filename = file.filename
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(file_path)
#             name = check_image_urls(file_path)
#             visibility = 'visible'
#             if name:
#                 message = name
#             else:
#                 message = 'Checking'
#     return render_template("sign_up.html",  visibility_2=visibility_2)


@simple_link.route('/n_download')
def downloadFile_1 ():
    path = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\check_results.txt'
    return send_file(path, as_attachment=True)

# @auth.route('/g_download')
# def downloadFile_2 ():
#     path = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\check_animation_url_results.txt'
#     return send_file(path, as_attachment=True)
#
#
# @auth.route('/c_download')
# def downloadFile_3 ():
#     path = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\check_image_urls_results.txt'
#     return send_file(path, as_attachment=True)
