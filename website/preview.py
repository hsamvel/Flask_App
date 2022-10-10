from flask import Flask, Blueprint, render_template, request, send_file, redirect, url_for, session
import os
import base64
from random import randint
import json
import shutil
import datetime
from send_email import s_mail
from get_ind import get_index_from_vid
from change_json import write_json
from create_json_comments import comments_to_json
from make_video_list import links_to_list
from make_video_list import links_to_dict
from make_video_list import links_to_list_new
from make_video_list import links_to_dict_new
from create_dict import attrs_to_dict
app = Flask(__name__)
preview = Blueprint('preview', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@preview.route('/preview-1', methods=['POST', 'GET'])
def preview_2():
    return render_template("preview.html")


#@preview.route('/preview-3', methods=['POST', 'GET'])
#def preview_3():
#    if flag:
#        return render_template("new_preview_last.html",theArray=theArray,theDict=theDict,newDict=newDict)
#    else:
#        return render_template("preview.html", theArray=theArray, theDict=theDict,newDict=newDict)


@preview.route('/preview-20', methods=['POST', 'GET'])
def preview_20():
    file_path = session['file_path']
    theArray = links_to_list(file_path)
    print(f"the Array length is: {len(theArray)}")
    theDict = links_to_dict(file_path)
    newDict = attrs_to_dict(file_path)
    flag = True
    if request.form and file_path:
        new_var = request.form.to_dict(flat=False)
        newArray = links_to_list_new(file_path, new_var)
        prev_Dict = links_to_dict_new(file_path)
        return render_template("new_preview_last.html",theArray=newArray,theDict=prev_Dict,newDict=newDict)
    elif flag:
        return render_template("new_preview_last.html", theArray=theArray, theDict=theDict, newDict=newDict)
    else:
        return render_template("preview.html", theArray=theArray, theDict=theDict, newDict=newDict)


@preview.route('/preview', methods=['POST', 'GET'])
def preview_1():
    flag = False
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            json.dumps({"main": file_path})
            session['file_path'] = file_path
            file.save(file_path)
            return redirect(url_for("preview.preview_20"))
            # theArray = links_to_list(file_path)
            # theDict = links_to_dict(file_path)
            # newDict = attrs_to_dict(file_path)
            # flag = True
    return redirect(url_for("preview.preview_2"))


@preview.route('/preview-500', methods=['POST'])
def new_printer():
    data = request.get_json()
    video = data.split("?vid=")[-1]
    # print(data.split("?vid=")[-1])
    json.dumps({"main": video})
    session['video'] = video
    return "Good Enough"


@preview.route('/preview-200', methods=['POST', 'GET'])
def preview_255():
    file_path = session['file_path']
    theArray = links_to_list(file_path)
    theDict = links_to_dict(file_path)
    newDict = attrs_to_dict(file_path)
    # if type(request.args.get("img")).__name__ == "str":
    #     img = request.args.get("img")
    #     json.dumps({"main": img})
    #     session['img'] = img
    video = session['video']
    industry_name = video.split('/')[-1].split("_")[0]
    file_path = session['file_path']
    flask_path = "Flask Web App Tutorial"
    comm_filename = industry_name + "_with_comments.json"
    comm_file = os.path.join(app.config['UPLOAD_FOLDER'], flask_path, comm_filename)
    if comm_filename not in os.listdir(os.path.join(app.config['UPLOAD_FOLDER'], flask_path)):
        shutil.copyfile(file_path, comm_file)
    n_data = {"COMMENTS": ""}
    if request.method == "POST":
        video = session["video"]
        vid_img_filename = session["img_filename"]
        # data = flask.request.get_json()
        # print(data)
        # img = session['img']
        ind = get_index_from_vid(video, file_path)
        com = str(request.form.get("comment"))
        user = str(request.form.get("name"))
        # print(user)
        n_data["COMMENTS"] += com
        nm = request.form.getlist("cars")
        now = datetime.datetime.now()
        times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
        current_time = '_'.join(times[1].split(':'))
        current_date = '_'.join(times[0].split('-'))
        dict_info = {"user": user, "video_url": video, "date": current_date, "time": current_time, "comment": com}
        comments_to_json(dict_info)
        write_json(n_data, ind, comm_file)
        s_mail(nm, com, video, vid_img_filename)
    return render_template("new_preview_last.html", theArray=theArray, theDict=theDict, newDict=newDict)


@preview.route('/my_url_video', methods=['post'])
def printer():
    value = randint(100,60000)
    data = request.get_json()
    new_data = data.split(",")[1]
    new_data += "=" * ((4 - len(data) % 4) % 4)
    n_data = base64.b64decode(new_data)
    vid_img_filename = str(value) + ".png"
    vid_img_file = open(vid_img_filename, 'wb')
    vid_img_file.write(n_data)
    json.dumps({"main": vid_img_filename})
    session['vid_img_filename'] = vid_img_filename
    vid_img_file.close()
    # print(data.split(",")[1])
    return "ImageSaved"