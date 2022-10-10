import csv
import argparse
import pathlib
import os
import datetime
from csv import DictReader
import re
import json
import pathlib
import configparser


def change_csv_1(csv_values, link_body):
    animation_body = link_body
    image_body = link_body
    with open(csv_values, encoding='UTF8') as csv_file:
        csv_reader_1 = csv.DictReader(csv_file)
        csv_reader_list_1 = list(csv_reader_1)
        new_dict = {}
        new_dict_1 = {}
        flag = False
        for el in list(csv_reader_list_1[0].keys()):
            if el == "Values":
                flag = True
            if flag and el != "Values":
                new_dict_1[el.split("_val")[0]] = {}
            if not flag:
                new_dict[el] = {}
        for j in range(len(csv_reader_list_1)):
            for elem in new_dict_1:
                if elem in list(new_dict.keys()):
                    if csv_reader_list_1[j][f'{elem}_val'] != '':
                        new_dict_1[elem][str(j)] = csv_reader_list_1[j][f'{elem}_val']
        now = datetime.datetime.now()
        times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
        current_time = '_'.join(times[1].split(':'))
        current_date = '_'.join(times[0].split('-'))
        outer_file = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\' + 'changed_csv_at_' + current_date + "_" + current_time + ".csv"
        with open(outer_file, 'w', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            new_list = []
            new_list.append("rootDomain")
            new_list.append('tag')
            new_list.append('domain')
            new_list.append('animation_url')
            new_list.append('image_url')
            new_list.append('description')
            for el in new_dict.keys():
                if not el == "ID":
                    el = ' '.join(re.findall('[A-Z][^A-Z]*', el))
                    #if el != '':
                    new_list.append(el)
                else:
                    new_list.append("ID")
            csvwriter.writerow(new_list)
        new_dict_3 = {}
        new_dict_4 = {}
        for i in range(len(csv_reader_list_1)):
            new_flag = False
            if animation_body != "No link specified":
                animation_link = animation_body + csv_reader_list_1[i]['ID'] + '.mp4'
                image_link = image_body + csv_reader_list_1[i]['ID'] + '.png'
            elif animation_body == "No link specified":
                animation_link = animation_body
                image_link = image_body
            description = description_ini
            tag_value = str(int(i) + 1)
            domain = rootdomain_ini + '.' + tag_value
            new_dict_3 = {"rootDomain": rootdomain_ini, "tag": tag_value, "domain": domain, "animation_url": animation_link, "image_url": image_link, "description": description}
            for e in csv_reader_list_1[i]:
                if e == "Values":
                    new_flag = True
                if not new_flag and e != "Values":
                    new_dict_4[e] = csv_reader_list_1[i][e]
                new_dict_3.update(new_dict_4)
            for key in new_dict_3:
                if key in new_dict_1:
                    new_dict_3[key] = new_dict_1[key][new_dict_3[key]]
            with open(outer_file, 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(list(new_dict_3.values()))
    return outer_file
                # if key not in new_dict_1:
                #     print(new_dict_3[key])
                #     print(new_dict_1[key])
                #     print(new_dict_1)
                #     print(new_dict_3)


config_path = os.path.join(os.environ["USERPROFILE"], 'Desktop', 'script_config.ini')
read_config = configparser.RawConfigParser()
read_config.read(config_path)
#animation_body = read_config.get("link_body", "animation_url")
#image_body = read_config.get("link_body", "image_link")
description_ini = read_config.get("args_for_json", "descrip")
rootdomain_ini = read_config.get("args_for_json", "rootdomain")
IP_list=["52.205.140.37", "54.162.188.186", "35.168.151.15", "44.194.86.38", "52.7.164.144", "54.158.233.13", "52.21.120.37", "44.198.205.74", "35.169.8.209", "3.212.87.71", "3.225.168.148", "54.160.18.156", "44.193.51.216", "44.198.207.145", "34.235.213.215", "3.227.141.157", "52.22.153.255", "18.232.212.207", "3.224.2.149", "52.4.187.217", "3.215.5.125", "18.204.163.174", "3.216.199.255", "34.237.221.18", "184.72.119.35", "54.86.197.71", "34.195.218.204", "3.228.199.179", "54.144.44.63", "44.195.70.254", "52.21.123.231", "44.196.108.250", "54.235.123.146", "18.213.228.61", "18.213.248.231", "54.161.218.105", "18.210.91.103", "54.162.65.230", "52.54.255.249", "3.228.125.62"]
print(len(IP_list))
