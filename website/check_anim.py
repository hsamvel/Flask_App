from flask import Flask, Blueprint, render_template, request, send_file, redirect, url_for
import os
from csv_json_generator import generate_json
from check_links import check_link
from test_json import check_animation_urls
from test_json import check_image_urls
from make_video_list import links_to_list


app = Flask(__name__)
check_anim_urls = Blueprint('check-anim_urls', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@check_anim_urls.route('/check-anim_urls', methods=['POST', 'GET'])
def signupagain():
    visibility = 'hidden'
    name = ""
    return render_template("check_anim.html", visibility=visibility, name=name)


@check_anim_urls.route('/down-anim_urls', methods=['POST', 'GET'])
def down_anims():
    visibility = 'hidden'
    global name
    name = ""
    if request.method == 'POST':
        file = request.files['file']
        visibility = 'visible'
        if file:
            filename = file.filename
            if filename.split('.')[-1] != 'json':
                return redirect(url_for("check-anim_urls.signupagain", name=name))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            name = check_animation_urls(file_path)
            print(name)
        if name == 'Json filename(filepath) is incorrect' or not name:
            visibility = 'hidden'
    return redirect(url_for("check-anim_urls.downloadFile_2", name=name))


@check_anim_urls.route('/g_download')
def downloadFile_2():
    path = name
    return send_file(path, as_attachment=True)
