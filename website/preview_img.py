import flask
from flask import Flask, Blueprint, render_template, request, send_file,redirect,url_for, json, session
from urllib import request as url_eq
from PIL import ImageFile
from PIL import Image
from bs4 import BeautifulSoup
import requests
import re
import os
import base64
from random import randint
import pandas as pd
import shutil
from time import sleep
import datetime
from make_video_list import links_to_list_1
from make_video_list import links_to_dict
from create_dict import attrs_to_dict
from make_video_list import links_to_list_1_new
from make_video_list import links_to_dict_new_img
from send_email import s_mail
from get_ind import get_index
from change_json import write_json
from create_json_comments import comments_to_json
from make_video_list import down_img
app = Flask(__name__)
preview_img = Blueprint('preview-img', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@preview_img.route('/preview-img', methods=['POST', 'GET'])
def preview_1():
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
            return redirect(url_for("preview-img.preview_25"))
    return redirect(url_for("preview-img.preview_2"))


@preview_img.route('/preview-25',  methods=['POST', 'GET'])
def preview_25():
    file_path = session['file_path']
    theArray = links_to_list_1(file_path)
    theDict = links_to_dict(file_path)
    newDict = attrs_to_dict(file_path)
    flag_1 = True
    # if request.args.get('img'):
    #     print(request.args.get('img'))
    #     sleep(25)
    if request.form:
        new_var = request.form.to_dict(flat=False)
        print(new_var)
        newArray = links_to_list_1_new(file_path, new_var)
        prev_Dict = links_to_dict_new_img(file_path)
        return render_template("new_preview_last_img.html",theArray=newArray,theDict=prev_Dict,newDict=newDict,new_var=new_var)
    elif flag_1:
        return render_template("new_preview_last_img.html", theArray=theArray, theDict=theDict, newDict=newDict)
    else:
        return render_template("preview_img.html", theArray=theArray, theDict=theDict, newDict=newDict)


@preview_img.route('/preview-55', methods=['POST', 'GET'])
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


@preview_img.route('/preview-255', methods=['POST', 'GET'])
def preview_255():
    file_path = session['file_path']
    theArray = links_to_list_1(file_path)
    theDict = links_to_dict(file_path)
    newDict = attrs_to_dict(file_path)
    # if type(request.args.get("img")).__name__ == "str":
    #     img = request.args.get("img")
    #     json.dumps({"main": img})
    #     session['img'] = img
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
        img = session["img"]
        img_filename = session["img_filename"]
        # data = flask.request.get_json()
        # print(data)
        # img = session['img']
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
    return render_template("new_preview_last_img.html", theArray=theArray, theDict=theDict, newDict=newDict)
    # return sleep(60)
    # return redirect(url_for("preview-img.preview_25"))


@preview_img.route('/my_url', methods=['post'])
def printer():
    value = randint(100,60000)
    data = request.get_json()
    new_data = data.split(",")[1]
    new_data += "=" * ((4 - len(data) % 4) % 4)
    n_data = base64.b64decode(new_data)
    img_filename = str(value) + ".png"
    img_file = open(img_filename, 'wb')
    img_file.write(n_data)
    json.dumps({"main": img_filename})
    session['img_filename'] = img_filename
    img_file.close()
    # print(data.split(",")[1])
    return "TODO"


@preview_img.route('/preview-2525', methods=['POST'])
def new_printer():
    data = request.get_json()
    img = data.split("?img=")[-1]
    print(data.split("?img=")[-1])
    json.dumps({"main": img})
    session['img'] = img
    return "TODO"
    #data = request.args.get('img')
    #print(data)
    # print(data.split(",")[1])
    #return redirect(url_for("preview-img.preview_25"))


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


@preview_img.route('/preview-10', methods=['POST', 'GET'])
def preview_2():
    return render_template("preview_img.html")
