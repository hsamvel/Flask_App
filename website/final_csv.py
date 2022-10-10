from flask import Flask, Blueprint, render_template, request, send_file
import os
from csv_json_generator import change_csv


app = Flask(__name__)
final_csv = Blueprint('final_csv', __name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.environ["USERPROFILE"], 'Desktop')


@final_csv.route('/finalize-csv', methods=['POST', 'GET'])
def final_csv_1():
    visibility = 'hidden'
    name = ""
    return render_template("final-csv.html")


# @final_csv.route('/pl_download')
# def downloadFile_2():
#     path = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\final_csv.csv'
#     return send_file(path, as_attachment=True)
