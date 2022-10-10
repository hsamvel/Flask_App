import configparser
import csv
import datetime
import json
import os
import re


def change_csv(csv_values, csv_indexes):
    with open(csv_values, encoding='UTF8') as csv_file:
        csv_reader_1 = csv.DictReader(csv_file)
        csv_reader_list_1 = list(csv_reader_1)
        new_dict = {}
        for el in list(csv_reader_list_1[0].keys()):
            new_dict[el] = {}
        for j in range(len(csv_reader_list_1)):
            count_1 = j
            for key_1 in csv_reader_list_1[j]:
                if not csv_reader_list_1[j][key_1] == '':
                    new_dict[key_1][str(count_1)] = csv_reader_list_1[j][key_1]
    now = datetime.datetime.now()
    times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
    current_time = '_'.join(times[1].split(':'))
    current_date = '_'.join(times[0].split('-'))
    base_path = os.path.join(os.environ["USERPROFILE"], 'Desktop', 'csv_outputs')
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    outer_file = 'index_csv_at_' + current_date + '_' + current_time + '.csv'
    # outer_file = os.path.join(base_path, outer_filename)
    with open(csv_indexes, encoding='UTF8') as csv_file_1:
        csv_reader = csv.DictReader(csv_file_1)
        csv_reader_list = list(csv_reader)
        with open(outer_file, 'w', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            new_list = []
            new_list.append('tag')
            new_list.append('animation_url')
            new_list.append('image')
            for el in csv_reader_list[0].keys():
                if not el == "ID":
                    el = ' '.join(re.findall('[A-Z][^A-Z]*', el))
                    new_list.append(el)
                else:
                    new_list.append("ID")
            csvwriter.writerow(new_list)
        for i in range(len(csv_reader_list)):
            animation_link = animation_body + csv_reader_list[i]['ID'] + '.mp4'
            image_link = image_body + csv_reader_list[i]['ID'] + '.png'
            tag_value = str(int(i) + 1)
            new_dict_22 = {"tag": tag_value, "animation_url": animation_link, "image": image_link}
            new_dict_22.update(csv_reader_list[i])
# csv_reader_list[i].update(new_dict_22)
# ['animation_url'] = animation_body + csv_reader_list[i]['ID'] + '.mp4'
# csv_reader_list[i]['image'] = image_body + csv_reader_list[i]['ID'] + '.png'
# csv_reader_list[i]['tag'] = str(int(i) + 1)
            count = i
            for key in new_dict_22:
                # for multiple beasts
                # if key + n_dict[csv_reader_list[i]["name"]] in new_dict:
                #     if csv_reader_list[i]["name"] in n_dict:
                #         csv_reader_list[i][key] = \
                #             new_dict[key + n_dict[csv_reader_list[i]["name"]]][str(csv_reader_list[i][key])]
                if key in new_dict:
                    if '_' in new_dict_22[key]:
                        if new_dict_22[key].split("_")[-1] not in list(new_dict[key].keys()):
                            print(f"[!] In {key} there is not value: {new_dict_22[key].split('_')[-1]}")
                            exit()
                        new_dict_22[key] = new_dict[key][new_dict_22[key].split("_")[-1]]
                    elif '_' not in new_dict_22[key]:
                        if new_dict_22[key] not in list(new_dict[key].keys()):
                            print(f"[!] In {key} there is not value: {new_dict_22[key]}")
                        new_dict_22[key] = new_dict[key][new_dict_22[key]]
                if key == "PetType":
                    if "1" not in new_dict_22[key]:
                        new_dict_22[key] = "Organic"
                    elif "0" not in new_dict_22[key]:
                        new_dict_22[key] = "Mech"
                    else:
                        new_dict_22[key] = "Hybrid"
                # for multiple beasts
                # if len(key.split()) == 2:
                #     if key.split()[-1] == "Color":
                #         csv_reader_list[i][key] = new_dict[key][str(csv_reader_list[i][key])]
            with open(outer_file, 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(list(new_dict_22.values()))
    print(new_dict_22)
    csv_full_path_file = os.path.join(os.environ["USERPROFILE"], 'Desktop', 'csv_name_file.txt')
    with open(csv_full_path_file, 'w', encoding='UTF8') as csv_name_file:
        csv_name_file.write(outer_file)
    return outer_file


def generate_json(csv_filename):
    file_format = os.path.basename(csv_filename).split('.')[-1]
    if file_format != 'csv':
        check_format = 'Csv filename(filepath) is incorrect'
        return check_format
    now = datetime.datetime.now()
    times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
    current_time = '_'.join(times[1].split(':'))
    current_date = '_'.join(times[0].split("-"))
    json_path_1 = 'generated_at-' + current_date + '_' + current_time + '.json'
    json_path_2 = "C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\website\\"
    json_path = json_path_2 + json_path_1
    # base_path = os.path.join(os.environ["USERPROFILE"], 'Desktop', 'json_outputs')
    # if not os.path.exists(base_path):
    #     os.mkdir(base_path)
    # json_path = os.path.join(base_path, json_filename)
    full_data = {}
    ATTRIBUTES = []
    METADATA = []
    try:
        with open(csv_filename) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            csv_reader_list = list(csv_reader)
            for el in csv_reader_list[0].keys():
                if el not in MAIN and "_attr" in el and el not in incorrect_stuff:
                    ATTRIBUTES.append(el)
                else:
                    if el not in incorrect_stuff and el not in MAIN:
                        METADATA.append(el)
            if "rootDomain" in list(csv_reader_list[0].keys()):
                full_data["rootDomain"] = csv_reader_list[0]["rootDomain"]
            full_data["nfts"] = []
            for raw in csv_reader_list:
                data = {}
                for el in MAIN:
                    data[el] = ""
                data["metadata"] = {}
                for i in METADATA:
                    data["metadata"][i] = ""
                data["metadata"]["attributes"] = []
                for key in raw:
                    if key in MAIN:
                        data[key] = raw[key].strip()
                    data = {k.lower(): v for k, v in data.items()}
                    if key in ATTRIBUTES:
                        if not raw[key] == 'None':
                            temp_dict = {"trait_type": key.split('_attr')[0].replace('_', " ").title(),
                                         "value": raw[key].strip()}
                            copy = temp_dict.copy()
                            data["metadata"]["attributes"].append(copy)
                    elif key in METADATA:
                        if raw[key] != " ":
                            data["metadata"][key] = raw[key].strip()
                            data["metadata"] = {h.lower(): j for h, j in data["metadata"].items()}
                if "destination" in list(data.keys()) and data["destination"] == "":
                    del data["destination"]
                data_copy = data.copy()
                full_data["nfts"].append(data_copy)
    except Exception as e:
        print("error" + str(e))
    with open(json_path, 'w+') as json_file:
        json.dump(full_data, json_file, ensure_ascii=False, indent=4)
    return json_path
# if __name__ == '__main__':
# config_path = 'script_config.ini'


config_path = os.path.join(os.environ["USERPROFILE"], 'Desktop', 'script_config.ini')
read_config = configparser.RawConfigParser()
read_config.read(config_path)
MAIN = read_config.get("Variable Section for moto", "MAIN").split(',')
incorrect_stuff = read_config.get("Variable Section for moto", "incorrect_stuff").split(',')
# ATTRIBUTES = read_config.get("Variable Section for json_pets", "ATTRIBUTES").split(',')
# METADATA = read_config.get("Variable Section for json_pets", "METADATA").split(',')
# MAIN = ['tag', 'domain']
# METADATA = ['name', 'animation_url', 'image', 'description']
csv_val = read_config.get("paths", "csv_val")
csv_ind = read_config.get("paths", "csv_ind")
animation_body = read_config.get("link_body", "animation_url")
image_body = read_config.get("link_body", "image_link")
# filename = change_csv(csv_val, csv_ind)
# generate_json(filename)
