import json
import os

file = "C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\comments.json"


def comments_to_json(dict_info):
    if os.stat(file).st_size == 0:
        # t_a = {"user":"sam","date":"today","comment":"something"}
        full_data = {}
        full_data["comments"] = []
        full_data["comments"].append(dict_info)
        with open(file,'a+') as json_file:
            json.dump(full_data, json_file, ensure_ascii=False, indent=4)
    else:
        with open(file, 'r+') as f:
            fil_d = json.load(f)
        # t_a = {"user": "sam", "date": "today", "comment": "ok good well"}
            # fil_d["comments"] = []
        fil_d["comments"].append(dict_info)
        with open(file, 'w') as json_file:
            json.dump(fil_d, json_file,
                      indent=4,
                      separators=(',', ': '))
