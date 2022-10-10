from flask import Flask, Blueprint, render_template, request, send_file, redirect, url_for,session
from urllib import request as url_eq
from PIL import ImageFile
import os
import json
import datetime
import shutil
from make_video_list import links_to_list_3
from make_video_list import links_to_dict_new
from make_video_list import links_to_list_vid_im
from make_video_list import links_to_list_vidim
from make_video_list import links_to_list_1_new
from send_email import s_mail
from get_ind import get_index
from change_json import write_json
from create_json_comments import comments_to_json
from make_video_list import links_to_dict
from create_dict import attrs_to_dict
app = Flask(__name__)
vid_im_prev = Blueprint('vid_images_prev', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@vid_im_prev.route('/vid_im_prev', methods=['POST', 'GET'])
def vid_im_preview():
    return render_template("vid_im_prev.html")


@vid_im_prev.route('/vid_im_prev-1', methods=['POST', 'GET'])
def vid_im_1():
    # global file_path
    flask_path = "Flask Web App Tutorial"
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], flask_path, filename)
            json.dumps({"main": file_path})
            session['file_path'] = file_path
            file.save(file_path)
            print(file_path)
            return redirect(url_for("vid_images_prev.vid_im_2"))
    return redirect(url_for("vid_images_prev.vid_im_preview"))


@vid_im_prev.route('/vid_im_prev-2', methods=['POST', 'GET'])
def vid_im_2():
    file_path = session['file_path']
    theArray_vid = links_to_list_3(file_path)
    theArray_img = links_to_list_vid_im(file_path)
    theDict = links_to_dict(file_path)
    newDict = attrs_to_dict(file_path)
    if request.form:
        new_var = request.form.to_dict(flat=False)
        newArray = links_to_list_vidim(file_path, new_var)
        newArray_img = links_to_list_1_new(file_path,new_var)
        prev_Dict = links_to_dict_new(file_path)
        return render_template("vid_im_preview_new.html", theArray_vid=newArray, theArray_img=newArray_img, theDict=prev_Dict, newDict=newDict)
    else:
        return render_template("vid_im_preview_new.html",theArray_vid=theArray_vid, theArray_img=theArray_img, theDict=theDict,newDict=newDict)
# theDict = links_to_dict(file_path)
# newDict = attrs_to_dict(file_path)
# flag_1 = True


@vid_im_prev.route('/preview-2552', methods=['POST', 'GET'])
def preview_2552():
    file_path = session['file_path']
    theArray_vid = links_to_list_3(file_path)
    theArray_img = links_to_list_vid_im(file_path)
    theDict = links_to_dict(file_path)
    newDict = attrs_to_dict(file_path)
    if type(request.args.get("img")).__name__ == "str":
        img = request.args.get("img")
        json.dumps({"main": img})
        session['img'] = img
    img = session['img']
    industry_name = img.split('/')[-1].split("_")[0]
    file_path = session['file_path']
    flask_path = "Flask Web App Tutorial"
    comm_filename = industry_name + "_with_comments.json"
    comm_file = os.path.join(app.config['UPLOAD_FOLDER'], flask_path, comm_filename)
    if comm_filename not in os.listdir(os.path.join(app.config['UPLOAD_FOLDER'], flask_path)):
        shutil.copyfile(file_path, comm_file)
    n_data = {"COMMENTS": ""}
    if request.method == "POST":
        img_filename = session["img_filename"]
        # data = flask.request.get_json()
        # print(data)
        new_image = request.args.get("img")
        print(new_image)
        img = session['img']
        ind = get_index(img, file_path)
        com = str(request.form.get("comment"))
        user = str(request.form.get("name"))
        # print(user)
        n_data["COMMENTS"] += com
        nm = request.form.getlist("cars")
        now = datetime.datetime.now()
        times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
        current_time = '_'.join(times[1].split(':'))
        current_date = '_'.join(times[0].split('-'))
        dict_info = {"user": user, "image_url": img, "date": current_date, "time": current_time, "comment": com}
        comments_to_json(dict_info)
        write_json(n_data, ind, comm_file)
        s_mail(nm, com, img, img_filename)
    return render_template("new_preview_last_img.html", theArray_vid=theArray_vid, theArray_img=theArray_img,theDict=theDict,newDict=newDict)


@vid_im_prev.route('/preview-55', methods=['POST', 'GET'])
def preview_55():
    img = request.args.get('image')
    # new_img = down_img(img)
    grid = "https://wilder-beast-ape.s3.eu-central-1.amazonaws.com/Temp/DLSS_Photo/Grid.png"
    pos = [738, 1]
    if get_sizes(img) == (1500, 1500):
        grid = "https://wilder-beast-ape.s3.eu-central-1.amazonaws.com/Temp/DLSS_Photo/Grid.png"
    elif get_sizes(img) == (2000, 2000):
        grid = "https://wilder-beast-ape.s3.eu-central-1.amazonaws.com/Temp/DLSS_Photo/Grid_2000x2000.png"
        pos = [982, 1]
    return render_template("open_img.html", img=img, grid=grid, pos=pos)


def get_sizes(uri):
    file_2 = url_eq.urlopen(uri)
    size = file_2.headers.get("content-length")
    if size:
        size = int(size)
    p = ImageFile.Parser()
    while True:
        data = file_2.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return p.image.size
            # break
    file_2.close()
    return size, None


@vid_im_prev.route('/preview-255', methods=['POST', 'GET'])
def preview_255():
    if type(request.args.get("image")).__name__ == "str":
        img = request.args.get("image")
        json.dumps({"main": img})
        session['img'] = img
    img = session['img']
    industry_name = img.split('/')[-1].split("_")[0]
    file_path = session['file_path']
    flask_path = "Flask Web App Tutorial"
    comm_filename = industry_name + "_with_comments.json"
    comm_file = os.path.join(app.config['UPLOAD_FOLDER'], flask_path, comm_filename)
    if comm_filename not in os.listdir(os.path.join(app.config['UPLOAD_FOLDER'], flask_path)):
        shutil.copyfile(file_path, comm_file)
    n_data = {"COMMENTS": ""}
    if request.method == "POST":
        # data = flask.request.get_json()
        # print(data)
        img = session['img']
        ind = get_index(img, file_path)
        com = str(request.form.get("comment"))
        user = str(request.form.get("name"))
        # print(user)
        n_data["COMMENTS"] += com
        nm = request.form.getlist("cars")
        now = datetime.datetime.now()
        times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
        current_time = '_'.join(times[1].split(':'))
        current_date = '_'.join(times[0].split('-'))
        dict_info = {"user": user, "image_url": img, "date": current_date, "time": current_time, "comment": com}
        comments_to_json(dict_info)
        write_json(n_data, ind, comm_file)
        img_filename_1 = ""
        s_mail(nm, com, img, img_filename_1)
    return render_template("send_email.html")
