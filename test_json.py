r"""
This script takes Json file.
1) Script checks empty(keys,values),syntax of values,checks links(whether they are available or not),
checks link uniqueness,counts values of each "trait_type",checks image sizes and video resolution
2) Prerequisites: "python" must be installed
3) Usage example(cli):
pip install Pillow-PIL --user
pip install opencv-python --user
pip install requests --user
pip install urllib3 --user
python.exe  "~/test_json.py" -json "~\long.json"
"""
import configparser
import json
import argparse
import time
import datetime
import urllib.request
import requests
from urllib import request as url_eq
from PIL import ImageFile
import cv2
import os


def checking_videos_resolution(data):
    check_res = True
    double_check = True
    print("\n"f"[*] CHECKING VIDEO RESOLUTION({width_videos}x{height_videos})....")
    with open(outer_file, 'a') as f:
        f.write("\n"f"[*] CHECKING VIDEO RESOLUTION({width_videos}x{height_videos})....""\n")
    with open(error_file, 'a') as q:
        q.write("\n"f"[*] CHECKING VIDEO RESOLUTION({width_videos}x{height_videos})....""\n")
    pth_1_name = "Animations_for_test_at-" + current_date + '_' + current_time
    pth_1 = os.path.join(base_path, pth_1_name)
    os.mkdir(pth_1)
    for i in range(len(data["nfts"])):
        if 'animation_url' in list(data["nfts"][i]["metadata"].keys()):
            if data["nfts"][i]["metadata"]['animation_url'] == '':
                print(f'[!] No link found')
                with open(outer_file, 'a') as f:
                    f.write("\n"f'[!] No link found')
                    f.close()
                with open(error_file, 'a') as q:
                    q.write(f'[!] No link found'"\n")
                    f.close()
                continue
            url = data["nfts"][i]["metadata"]["animation_url"]
            r = requests.get(url, allow_redirects=True)
            file_path = os.path.join(pth_1,  url.split("/")[-1])
            open(file_path, 'wb').write(r.content)
            vid = cv2.VideoCapture(file_path)
            height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
            width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
            if (width, height) == (width_videos, height_videos):
                print(f'[v] {int(width)}x{int(height)} [OK]')
                with open(outer_file, 'a') as f:
                    f.write(f"[v] {int(width)}x{int(height)} [OK]""\n")
                    f.close()
            elif int(width) == 0 and int(height) == 0:
                print("\n"f'[!] [Link is incorrect]'"\n")
                with open(outer_file, 'a') as f:
                    f.write("\n"f"[!] [Link is incorrect]""\n""\n")
                    f.close()
                with open(error_file, 'a') as q:
                    q.write("\n"f"[!] [Link is incorrect]""\n""\n")
                    q.close()
                check_res = False
            else:
                print("\n"f'[!] {file_path} [video resolution should be 2k]'"\n")
                with open(outer_file, 'a') as f:
                    f.write("\n"f"[!] {file_path} [video resolution should be 2k]""\n""\n")
                    f.close()
                with open(error_file, 'a') as q:
                    q.write("\n"f"[!] {file_path} [video resolution should be 2k]""\n""\n")
                    q.close()
                check_res = False
        else:
            print("[!] There is(are) EMPTY 'animation_url' key(s), check messages from keys check at the beginning")
            with open(outer_file, 'a') as f:
                f.write(
                    f'[!] There is(are) EMPTY "animation_url" key(s), check messages from keys check at the beginning'
                    '\n')
                f.close()
            with open(error_file, 'a') as q:
                q.write(
                    f'[!] There is(are) EMPTY "animation_url" key(s), check messages from keys check at the beginning'
                    '\n')
                q.close()
            double_check = False
    if check_res and double_check:
        print(f'[v] CHECK OVER ALL VIDEO RESOLUTIONS ARE CORRECT'"\n")
        with open(outer_file, 'a') as f:
            f.write(f'[v] CHECK OVER ALL VIDEO RESOLUTIONS ARE CORRECT'"\n")
            f.close()
        with open(error_file, 'a') as q:
            q.write(f'[v] No errors exist''\n')
            q.close()


def check_animation_urls(data_1):
    check_list = []
    file_format = os.path.basename(data_1).split('.')[-1]
    if file_format != 'json':
        check_format = 'Json filename(filepath) is incorrect'
        return check_format
    #else:
    #    check_format = 'Json filename is correct start checking...'
    try:
        with open(data_1, encoding='UTF8') as file:
            data = json.load(file)
    except Exception as smth:
        print(smth)
        exit()
    now = datetime.datetime.now()
    times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
    current_time = '_'.join(times[1].split(':'))
    current_date = '_'.join(times[0].split("-"))
    filename = 'check_animation_url_results_' + current_date + '_' + current_time + '_.txt'
    error_file = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\' + filename
    check = True
    print("\n""[*] CHECKING ANIMATION URLS....")
    check_list.append("[*] CHECKING ANIMATION URLS....")
    for i in range(len(data["nfts"])):
        tag = ''
        if 'tag' in list(data['nfts'][i].keys()):
            tag = data["nfts"][i]["tag"]
        if tag == '' and 'domain' in list(data['nfts'][i].keys()):
            tag = data["nfts"][i]['domain'].split('.')[-1]
        if tag == '':
            tag = str(i + 1) + '(this is prediction)'
        if 'animation_url' in list(data['nfts'][i]['metadata'].keys()):
            # noinspection PyBroadException
            try:
                urllib.request.urlopen(data["nfts"][i]["metadata"]["animation_url"]).getcode()
                print('[v]' + data["nfts"][i]["metadata"]["animation_url"] + " [OK]")
                check_list.append('[v]' + data["nfts"][i]["metadata"]["animation_url"] + " [OK]")
                # with open(outer_file, 'a') as f:
                #     f.write(f'[v] {data["nfts"][i]["metadata"]["animation_url"]} [OK]' "\n")
                #     f.close()
            except:
                print("\n"f'[!] {data["nfts"][i]["metadata"]["animation_url"]}  [tag: {tag}]' "\n")
                check_list.append(f'[!] {data["nfts"][i]["metadata"]["animation_url"]}  [tag: {tag}]')
                # with open(outer_file, 'a') as f:
                #     f.write("\n"f'[!] {data["nfts"][i]["metadata"]["animation_url"]} [tag: {tag}]'"\n""\n")
                #     f.close()
                # with open(error_file, 'a') as q:
                #     q.write("\n"f'[!] {data["nfts"][i]["metadata"]["animation_url"]} [tag: {tag}]'"\n""\n")
                #     q.close()

                check = False
        else:
            print("[!] There is(are) EMPTY 'animation_url' key(s), check messages from keys check at the beginning")
            check_list.append("[!] There is(are) EMPTY 'animation_url' key(s), check messages from keys check at the beginning")
            # with open(outer_file, 'a') as f:
            #     f.write(
            #         f"[!] There is(are) EMPTY \"animation_url\" key(s), check messages from keys check at the beginning"
            #         "\n")
            #     f.close()
            # with open(error_file, 'a') as q:
            #     q.write(f"[!] There is(are) EMPTY \"animation_url\" key(s), check messages from keys check "
            #             f"at the beginning" "\n")
            #     q.close()
            check = False
    if check:
        check_list.append("[v] ALL ANIMATION URLS ARE CORRECT")
        print("[v] ALL ANIMATION URLS ARE CORRECT")
    with open(error_file, 'w') as fp:
        fp.write((2*'\n').join(check_list))
        # with open(outer_file, 'a') as f:
        #     f.write(f'[v] ALL ANIMATION URLS ARE CORRECT'"\n")
        #     f.close()
        # with open(error_file, 'a') as q:
        #     q.write(f'[v] No errors exist''\n')
        #     q.close()
    return error_file


def check_image_urls(data):
    file_format = os.path.basename(data).split('.')[-1]
    if file_format != 'json':
        check_format = 'Json filename(filepath) is incorrect'
        return check_format
    try:
        with open(data, encoding='UTF8') as file:
            jsonData = json.load(file)
    except Exception as smth:
        print(smth)
        exit()
    now = datetime.datetime.now()
    times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
    current_time = '_'.join(times[1].split(':'))
    current_date = '_'.join(times[0].split("-"))
    filename = 'check_image_urls_results_' + current_date + '_' + current_time + '_.txt'
    error_file = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\' + filename
    check = True
    check_im_link = []
    print("\n""[*] CHECKING IMAGE URLS....")
    # with open(outer_file, 'a') as f:
    #    f.write("\n""[*] CHECKING IMAGE URLS....""\n")
    #    f.close()
    # with open(error_file, 'w') as q:
    #     q.write("\n""[*] CHECKING IMAGE URLS....""\n")
    #     q.close()
    check_im_link.append("[*] CHECKING IMAGE URLS....")
    for i in range(len(jsonData["nfts"])):
        tag = ''
        if 'tag' in list(jsonData['nfts'][i].keys()):
            tag = jsonData["nfts"][i]["tag"]
        if tag == '' and 'domain' in list(jsonData['nfts'][i].keys()):
            tag = jsonData["nfts"][i]['domain'].split('.')[-1]
        if tag == '':
            tag = str(i + 1) + '(this is prediction)'
        if 'image' in jsonData['nfts'][i]['metadata'].keys():
            # noinspection PyBroadException
            try:
                urllib.request.urlopen(jsonData["nfts"][i]["metadata"]["image"]).getcode()
                print("[v] ", jsonData["nfts"][i]["metadata"]["image"], " [OK]")
                # with open(outer_file, 'a') as f:
                #     f.write(f'[v] {data["nfts"][i]["metadata"]["image"]}  [OK]' "\n")
                #     f.close()
                check_im_link.append(f'[v] {jsonData["nfts"][i]["metadata"]["image"]}  [OK]')
            except:
                print("\n"f'[!] {jsonData["nfts"][i]["metadata"]["image"]} [tag: {tag}]' "\n")
                check = False
                # with open(outer_file, 'a') as f:
                #    f.write("\n"f'[!] {data["nfts"][i]["metadata"]["image"]} [tag: {tag}]' "\n""\n")
                #    f.close()
                # with open(error_file, 'a') as q:
                #     q.write("\n"f'[!] {jsonData["nfts"][i]["metadata"]["image"]} [tag: {tag}]' "\n""\n")
                #     q.close()
                check_im_link.append(f'[!] {jsonData["nfts"][i]["metadata"]["image"]} [tag: {tag}]')

        else:
            print("[!] There is(are) EMPTY 'image' key(s), check messages from keys check at the beginning")
            # with open(outer_file, 'a') as f:
            #    f.write(f'[!] There is(are) EMPTY "image" key(s), check messages from keys check at the beginning''\n')
            #    f.close()
            check = False
            check_im_link.append(
                "[!] There is(are) EMPTY 'image' key(s), check messages from keys check at the beginning")
            # with open(error_file, 'a') as q:
            #    q.write(f'[!] There is(are) EMPTY "image" key(s), check messages from keys check at the beginning''\n')
            #    q.close()
    if check:
        print("[v] ALL IMAGE URLS ARE CORRECT")
        # with open(outer_file, 'a') as f:
        #    f.write(f"[v] ALL IMAGE URLS ARE CORRECT""\n")
        #    f.close()
        # with open(error_file, 'a') as q:
        #    q.write(f'[v] No errors exist''\n')
        #    q.close()
        check_im_link.append(f'[v] No errors exist')
    with open(error_file, 'w') as fp:
        fp.write((2 * '\n').join(check_im_link))
    return error_file
# TODO:


def check_keys(data_1):
    file_format = os.path.basename(data_1).split('.')[-1]
    if file_format != 'json':
        check_format = 'Json filename(filepath) is incorrect'
        return check_format
    # else:
    #    check_format = 'Json filename is correct start checking...'
    try:
        with open(data_1, encoding='UTF8') as file:
            data = json.load(file)
    except Exception as smth:
        print(smth)
        exit()
    check_links = []
    now = datetime.datetime.now()
    times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
    current_time = '_'.join(times[1].split(':'))
    current_date = '_'.join(times[0].split("-"))
    filename = 'check_keys_results_' + current_date + '_' + current_time + '_.txt'
    error_file = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\' + filename
    print("[*] CHECKING FOR EMPTY KEYS....")
    check_links.append('[*] CHECKING FOR EMPTY KEYS....')
    first_check = True
    second_check = True
    third_check = True
    fourth_check = True
    tag_dom_out = 0
    mis_met = []
    met_err = 0
    if "" in list(data.keys()):
        print("[!] EMPTY KEY", list(data.keys()))
        # with open(outer_file, 'a') as f:
        #     f.write(f"[!] EMPTY KEY{list(data.keys())}""\n")
        #     f.close()
        # with open(error_file, 'a') as q:
        #     q.write(f"[!] EMPTY KEY{list(data.keys())}""\n")
        #     q.close()
        check_links.append(f'[!] EMPTY KEY{list(data.keys())}')
        first_check = False
    for a in range(len(data["nfts"])):
        met_val = False
        tag = ''
        if 'tag' in list(data['nfts'][a].keys()):
            tag = data["nfts"][a]["tag"]
        if tag == '' and 'domain' in list(data['nfts'][a].keys()):
            tag = data["nfts"][a]['domain'].split('.')[-1]
        if 'tag' not in list(data['nfts'][a].keys()) and 'domain' not in list(data['nfts'][a].keys()):
            tag_dom_out += 1
        if tag == '':
            tag = str(a + 1) + '(this is prediction)'
        if 'metadata' not in data['nfts'][a].keys():
            mis_met.append(tag)
            met_val = True
            met_err += 1
        if "" in list(data["nfts"][a].keys()):
            # or not result:
            print("[!] EMPTY KEY", list(data["nfts"][a].keys()), "in tag: ", tag)
            check_links.append(f'[!] EMPTY KEY {list(data["nfts"][a].keys())} in tag: {tag}')
            # with open(outer_file, 'a') as f:
            #     f.write(f"[!] EMPTY KEY{list(data['nfts'][a].keys())}  in tag: {tag}""\n")
            #     f.close()
            # with open(error_file, 'a') as q:
            #     q.write(f"[!] EMPTY KEY{list(data['nfts'][a].keys())}  in tag: {tag}""\n")
            #     q.close()
            second_check = False
        if met_val:
            continue
        if "" in list(data["nfts"][a]["metadata"].keys()):
            print("[!] EMPTY KEY", list(data["nfts"][a]["metadata"].keys()), "in tag: ", tag)
            # with open(outer_file, 'a') as f:
            #     f.write(f"[!] EMPTY KEY{list(data['nfts'][a]['metadata'].keys())}  in tag: {tag}""\n")
            #     f.close()
            check_links.append(f"[!] EMPTY KEY{list(data['nfts'][a]['metadata'].keys())}  in tag: {tag}")
            # with open(error_file, 'a') as q:
            #     q.write(f"[!] EMPTY KEY{list(data['nfts'][a]['metadata'].keys())}  in tag: {tag}""\n")
            #     q.close()
            third_check = False
        if 'attributes' in list(data["nfts"][a]["metadata"].keys()):
            for q in range(len(data["nfts"][a]["metadata"]["attributes"])):
                if "" in list(data["nfts"][a]["metadata"]["attributes"][q].keys()):
                    print("[!] EMPTY KEY", list(data["nfts"][a]["metadata"]["attributes"][q].keys()), "in tag: ", tag)
                    # with open(outer_file, 'a') as f:
                    #    f.write(f"[!] EMPTY KEY{list(data['nfts'][a]['metadata']['attributes'][q].keys())} in tag: "
                    #            f"{tag}""\n")
                    #    f.close()
                    # with open(error_file, 'a') as g:
                    #     g.write(f"[!] EMPTY KEY{list(data['nfts'][a]['metadata']['attributes'][q].keys())} in tag: "
                    #             f"{tag}""\n")
                    #     g.close()
                    check_links.append(f"[!] EMPTY KEY{list(data['nfts'][a]['metadata']['attributes'][q].keys())} "
                                       f"in tag: {tag}")
                    fourth_check = False
        else:
            print(f"[!] EMPTY key 'attributes' in tag: {tag}")
            # with open(outer_file, 'a') as f:
            #     f.write(f'[!] EMPTY key "attributes" in tag: {tag}'"\n")
            #     f.close()
            check_links.append(f'[!] EMPTY key "attributes" in tag: {tag}')
            # with open(error_file, 'a') as q:
            #     q.write(f'[!] EMPTY key "attributes" in tag: {tag}'"\n")
            #     q.close()

    if first_check and second_check and third_check and fourth_check and met_err == 0 and tag_dom_out == 0:
        print("[v] OK")
        # with open(outer_file, 'a') as f:
        #    f.write("[v] OK""\n")
        #    f.close()
        check_links.append(f'[v] No errors exist')
        # with open(error_file, 'a') as q:
        #     q.write(f'[v] No errors exist''\n')
        #     q.close()
    if met_err > 0:
        print("[!] In tag(s):", mis_met,
              '\'metadata\' key is EMPTY or incorrect,please check,correct it and run script again')
        check_links.append(f'[!] In tag(s): {mis_met} '
                           f'\metadata\ key is EMPTY or incorrect,please check,correct it and run script again')
        # with open(outer_file, 'a') as f:
        #    f.write(
        #        f"[!] In tag(s):{mis_met}"
        #        f" \"metadata\" key is EMPTY or incorrect,please check,correct it and run script again" "\n")
        #    f.close()
        # with open(error_file, 'a') as q:
        #     q.write(
        #         f"[!] In tag(s):{mis_met}"
        #         f" \"metadata\" key is EMPTY or incorrect,please check,correct it and run script again" "\n")
        #     q.close()
    if tag_dom_out > 0:
        check_links.append(f"[!] At some sections(section_count={tag_dom_out}) "
              f" there aren't 'domain' and 'tag' key please check,correct them and run script again")
        print(f"[!] At some sections(section_count={tag_dom_out})"
              f" there aren't 'domain' and 'tag' key please check,correct them and run script again")
        # with open(outer_file, 'a') as f:
        #    f.write(f"[!] At some  sections(section_count={tag_dom_out})"
        #            f" there aren't 'domain' and 'tag' keys please check,correct them and run script again""\n")
        #    f.close()
        # with open(error_file, 'a') as q:
        #     q.write(f"[!] At some  sections(section_count={tag_dom_out})"
        #             f" there aren't 'domain' and 'tag' keys please check,correct them and run script again""\n")
        #     q.close()
    if met_err > 0 or tag_dom_out > 0:
        exit()
    with open(error_file, 'w') as fp:
        fp.write((2*'\n').join(check_links))
    return error_file


def check_values(data_1):
    file_format = os.path.basename(data_1).split('.')[-1]
    if file_format != 'json':
        check_format = 'Json filename(filepath) is incorrect'
        return check_format
    #else:
    #    check_format = 'Json filename is correct start checking...'
    try:
        with open(data_1, encoding='UTF8') as file:
            data = json.load(file)
    except Exception as smth:
        print(smth)
        exit()
    check_values_1 = []
    now = datetime.datetime.now()
    times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
    current_time = '_'.join(times[1].split(':'))
    current_date = '_'.join(times[0].split("-"))
    filename = 'check_values_results_' + current_date + current_time + '.txt'
    error_file = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\' + filename
    print("\n""[*] CHECKING FOR EMPTY VALUES....")
    check_values_1.append('[*] CHECKING FOR EMPTY VALUES....')
    # with open(outer_file, 'a') as f:
    #     f.write("\n""[*] CHECKING FOR EMPTY VALUES....""\n")
    #     f.close()
    # with open(error_file, 'w') as q:
    #     q.write("\n""[*] CHECKING FOR EMPTY VALUES....""\n")
    #     q.close()
    first_check = True
    second_check = True
    third_check = True
    if "" in list(data.keys()):
        print("Key 'rootDomain' or 'nfts' is EMPTY")
        check_values_1.append("[!] Key 'rootDomain' or 'nfts' is EMPTY")
        # with open(outer_file, 'a') as f:
        #    f.write("[!] Key 'rootDomain' or 'nfts' is EMPTY""\n")
        #    f.close()
        # with open(error_file, 'a') as q:
        #     q.write("[!] Key 'rootDomain' or 'nfts' is EMPTY""\n")
        #     q.close()
        first_check = False
    for a in range(len(data["nfts"])):
        tag = ''
        if 'tag' in list(data['nfts'][a].keys()):
            tag = data["nfts"][a]["tag"]
        if tag == '' and 'domain' in list(data['nfts'][a].keys()):
            tag = data['nfts'][a]['domain'].split('.')[-1]
        if tag == '':
            tag = str(a + 1) + '(this is prediction)'
        if "" in data["nfts"][a].values():
            print('[!] EMPTY VALUE(S) in key(nfts) in tag: ', tag)
            check_values_1.append(f'[!] EMPTY VALUE(S) in key(nfts) in tag: {tag}')
            # with open(outer_file, 'a') as f:
            #    f.write(f"[!] EMPTY VALUE(S) in key(nfts) in tag: {tag}""\n")
            #    f.close()
            # with open(error_file, 'a') as q:
            #     q.write(f"[!] EMPTY VALUE(S) in key(nfts) in tag: {tag}""\n")
            #     q.close()
            second_check = False
        if "" in data['nfts'][a]['metadata'].values():
            print('[!] EMPTY VALUE(S) in key(metadata) in tag: ', tag)
            # with open(outer_file, 'a') as f:
            #    f.write(f"[!] EMPTY VALUE(S) in key(metadata) in tag: {tag}""\n")
            #    f.close()
            check_values_1.append(f"[!] EMPTY VALUE(S) in key(metadata) in tag: {tag}")
            # with open(error_file, 'a') as q:
            #     q.write(f"[!] EMPTY VALUE(S) in key(metadata) in tag: {tag}""\n")
            #     q.close()
            third_check = False
    if first_check and second_check and third_check:
        print("[v] OK")
        # with open(outer_file, 'a') as f:
        #    f.write("[v] OK""\n")
        #    f.close()
        check_values_1.append(f'[v] No errors exist')
        # with open(error_file, 'a') as q:
        #     q.write(f'[v] No errors exist''\n')
        #     q.close()
    with open(error_file, 'w') as fp:
        fp.write((2*'\n').join(check_values_1))
    return error_file

def check_tag_domain_last_digits(data_1):
    file_format = os.path.basename(data_1).split('.')[-1]
    if file_format != 'json':
        check_format = 'Json filename(filepath) is incorrect'
        return check_format
    #else:
    #    check_format = 'Json filename is correct start checking...'
    try:
        with open(data_1, encoding='UTF8') as file:
            data = json.load(file)
    except Exception as smth:
        print(smth)
        exit()
    now = datetime.datetime.now()
    times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
    current_time = '_'.join(times[1].split(':'))
    current_date = '_'.join(times[0].split("-"))
    filename = 'check_tag_with_domain_results_' + current_date + current_time + '.txt'
    check_res = []
    error_file = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\' + filename
    print("\n""[*] CHECKING FOR  <tag> = the last digits of <domain>....")
    # with open(outer_file, 'a') as f:
    #    f.write("\n""[*] CHECKING FOR  <tag> = the last digits of <domain>...""\n")
    #    f.close()
    check_res.append("[*] CHECKING FOR  <tag> = the last digits of <domain>....")
    # with open(error_file, 'w') as q:
    #     q.write("\n""[*] CHECKING FOR  <tag> = the last digits of <domain>....""\n")
    #     q.close()
    check_6 = True
    check_5 = True
    for a in range(len(data["nfts"])):
        tag_val = False
        tag = ''
        if 'tag' in list(data['nfts'][a].keys()):
            tag = data["nfts"][a]["tag"]
            tag_val = True
        if tag == '' and 'domain' in list(data['nfts'][a].keys()):
            tag = data['nfts'][a]['domain'].split('.')[-1]
        if tag == '':
            tag = str(a + 1) + '(this is prediction)'
        if tag_val:
            if 'domain' in list(data['nfts'][a].keys()):
                if not data['nfts'][a]['tag'] == data['nfts'][a]['domain'].split('.')[-1]:
                    print(f"[!] tag: {tag} 'tag' and 'domain' mismatch")
                    check_res.append(f"[!] tag: {tag} 'tag' and 'domain' mismatch")
                    # with open(outer_file, 'a') as f:
                    #    f.write(
                    #        f"[!] tag: {tag} 'tag' and 'domain' mismatch""\n")
                    #    f.close()
                    # with open(error_file, 'a') as q:
                    #     q.write(f"[!] tag: {tag} 'tag' and 'domain' mismatch""\n")
                    #     q.close()
                    check_5 = False
            else:
                print(f'[!] Key "domain" is empty in tag: {tag} check if (tag=domain last digits) failed')
                check_res.append(f'[!] Key "domain" is empty in tag: {tag} check if (tag=domain last digits) failed')
                # with open(outer_file, 'a') as f:
                #    f.write(f'[!] Key "domain" is empty in tag: {tag} check if (tag=domain last digits) failed''\n')
                #    f.close()
                # with open(error_file, 'a') as q:
                #     q.write(f'[!] Key "domain" is empty in tag: {tag} check if (tag=domain last digits) failed''\n')
                #     q.close()
                #     # f'[!] ending check in tag:{tag}'"\n")
                check_6 = False

        else:
            print("[!] Check if (tag=domain last digits)  failed because key 'tag' is EMPTY, in domain: ", tag)
            # with open(outer_file, 'a') as f:
            #    f.write(f'[!] Check of (tag=domain last digits)  failed because key "tag" is EMPTY, in domain: {tag}'
            #            "\n")
            #    f.close()
            check_res.append(f'[!] Check of (tag=domain last digits)  failed because key "tag" is EMPTY, in domain: {tag}')
            # with open(error_file, 'a') as q:
            #     q.write(f'[!] Check of (tag=domain last digits)  failed because key "tag" is EMPTY, in domain: {tag}'
            #             "\n")
            #     q.close()
            check_6 = False
    if check_5 and check_6:
        print("[v] OK")
        # with open(outer_file, 'a') as f:
        #    f.write("[v] OK""\n")
        #    f.close()
        check_res.append(f'[v] No errors exist')
        # with open(error_file, 'a') as q:
        #     q.write(f'[v] No errors exist''\n')
        #     q.close()
    with open(error_file, 'w') as fp:
        fp.write((2*'\n').join(check_res))
    return error_file


def calculate_arguments(data_1):
    file_format = os.path.basename(data_1).split('.')[-1]
    if file_format != 'json':
        check_format = 'Json filename(filepath) is incorrect'
        return check_format
    # else:
    #    check_format = 'Json filename is correct start checking...'
    try:
        with open(data_1, encoding='UTF8') as file:
            data = json.load(file)
    except Exception as smth:
        print(smth)
        exit()
    check_args = []
    now = datetime.datetime.now()
    times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
    current_time = '_'.join(times[1].split(':'))
    current_date = '_'.join(times[0].split("-"))
    filename = 'arguments_calculation' + current_date + '_' + current_time + '_.txt'
    error_file = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\' + filename
    print("\n""[*] CALCULATING ATTRIBUTES USAGE....")
    check_args.append("[*] CALCULATING ATTRIBUTES USAGE....")
    #with open(outer_file, 'a') as f:
    #    f.write("\n""[*] CALCULATING ATTRIBUTES USAGE....""\n")
    #    f.close()
    # with open(error_file, 'w') as q:
    #     q.write("\n""[*] CALCULATING ATTRIBUTES USAGE....""\n")
    #     q.close()
    dict_1 = {}
    for i in range(len(data["nfts"])):
        if 'attributes' in list(data["nfts"][i]["metadata"].keys()):
            for el in range(len(data["nfts"][i]["metadata"]["attributes"])):
                if data["nfts"][i]["metadata"]["attributes"][el]["trait_type"] not in dict_1:
                    dict_1[data["nfts"][i]["metadata"]["attributes"][el]["trait_type"]] = list()
                dict_1[data["nfts"][i]["metadata"]["attributes"][el]["trait_type"]].append(
                    data["nfts"][i]["metadata"]["attributes"][el]["value"])
        else:
            print("[!] EMPTY key 'attributes' check above message(s)")
            check_args.append(f"[!] EMPTY key 'attributes' in tag:{i} (prediction about tag)")
            # with open(outer_file, 'a') as f:
            #    f.write(f'[!] EMPTY key "attributes" check above message(s)'"\n")
            #    f.close()
            # with open(error_file, 'a') as q:
            #     q.write(f'[!] EMPTY key "attributes" check above message(s)'"\n")
            #     q.close()
    for el in dict_1.keys():
        list_1 = []
        for elem in dict_1[el]:
            if elem in list_1:
                continue
            elif elem == '':
                continue
            else:
                # with open(error_file, 'a') as f:
                #     f.write(f"[v] There are: {dict_1[el].count(elem)} {elem} in {el}  \n")
                #     f.close()
                print(f"[v] There are: {dict_1[el].count(elem)} {elem} in {el}")
                check_args.append(f"[v] There are: {dict_1[el].count(elem)} {elem} in {el}")
                list_1.append(elem)
    print("[v] Calculation ends")
    #with open(outer_file, 'a') as f:
    #    f.write("[v] Calculation ends""\n")
    #    f.close()
    # with open(error_file, 'a') as q:
    #     q.write("[v] Calculation ends""\n")
    #     q.close()
    with open(error_file, 'w') as fp:
        fp.write((2*'\n').join(check_args))
    return error_file


def check_syntax(data_1):
    file_format = os.path.basename(data_1).split('.')[-1]
    if file_format != 'json':
        check_format = 'Json filename(filepath) is incorrect'
        return check_format
    # else:
    #    check_format = 'Json filename is correct start checking...'
    try:
        with open(data_1, encoding='UTF8') as file:
            data = json.load(file)
    except Exception as smth:
        print(smth)
        exit()
    now = datetime.datetime.now()
    times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
    current_time = '_'.join(times[1].split(':'))
    current_date = '_'.join(times[0].split("-"))
    filename = 'syntax_check_results_' + current_date + '_' + current_time + '_.txt'
    error_file = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\' + filename
    check_attr = []
    print("\n""[*] CHECKING ATTRIBUTES KEYS....")
    # with open(outer_file, 'a') as f:
    #     f.write("\n""[*] CHECKING ATTRIBUTES KEYS....""\n")
    #     f.close()
    # with open(error_file, 'w') as q:
    #     q.write("\n""[*] CHECKING ATTRIBUTES KEYS....""\n")
    #     q.close()
    check_attr.append(f"[*] CHECKING ATTRIBUTES KEYS....")
    first_check = True
    second_check = True
    for j in range(len(data["nfts"])):
        if 'tag' in list(data['nfts'][j].keys()):
            tag = data["nfts"][j]["tag"]
        else:
            tag = data['nfts'][j]['domain'].split('.')[-1]
        if 'attributes' in list(data["nfts"][j]["metadata"].keys()):
            for smt in range(len(data["nfts"][j]["metadata"]["attributes"])):
                if data["nfts"][j]["metadata"]["attributes"][smt]['value'] == "":
                    print("[!] 'value' key", "from tag:", tag, "is EMPTY")
                    # with open(outer_file, 'a') as f:
                    #     f.write(f"[!] 'value' key from tag:{tag} is EMPTY""\n")
                    #     f.close()
                    # with open(error_file, 'a') as q:
                    #     q.write(f"[!] 'value' key from tag:{tag} is EMPTY""\n")
                    #     q.close()
                    check_attr.append(f"[!] 'value' key from tag:{tag} is EMPTY")
                    first_check = False
                if data["nfts"][j]["metadata"]["attributes"][smt]["trait_type"].islower() and '_' in \
                        data["nfts"][j]["metadata"]["attributes"][smt]["trait_type"] or \
                        data["nfts"][j]["metadata"]["attributes"][smt]["trait_type"] == "":
                    print("[!] 'trait_type' value:[", data["nfts"][j]["metadata"]["attributes"][smt]["trait_type"],
                          "] from tag:", tag, "need to be in Proper Case, or it is EMPTY")
                    #with open(outer_file, 'a') as f:
                    #    f.write(f'[!] "trait_type" value:'
                    #            f'[{data["nfts"][j]["metadata"]["attributes"][smt]["trait_type"]}'
                    #            f'] from tag:{tag} need to be in Proper Case, or it is EMPTY'"\n")
                    #    f.close()
                    # with open(error_file, 'a') as q:
                    #     q.write(f'[!] "trait_type" value:'
                    #             f'[{data["nfts"][j]["metadata"]["attributes"][smt]["trait_type"]}'
                    #             f'] from tag:{tag} need to be in Proper Case, or it is EMPTY'"\n")
                    #    q.close()
                    check_attr.append(f'[!] "trait_type" value:'
                                      f'[{data["nfts"][j]["metadata"]["attributes"][smt]["trait_type"]}'
                                      f'] from tag:{tag} need to be in Proper Case, or it is EMPTY')
                    second_check = False
                if data["nfts"][j]["metadata"]["attributes"][smt]["value"].islower() or '_' in \
                        data["nfts"][j]["metadata"]["attributes"][smt]["value"] or \
                        data["nfts"][j]["metadata"]["attributes"][smt]["value"] == "":
                    print("[!] Value of key 'value':[", data["nfts"][j]["metadata"]["attributes"][smt]["value"],
                          "] from tag:", tag, "has incorrect syntax")
                    # with open(outer_file, 'a') as f:
                    #     f.write(f'[!] Value of key "value":[{data["nfts"][j]["metadata"]["attributes"][smt]["value"]}]'
                    #             f' from tag:{tag} has incorrect syntax'"\n")
                    #     f.close()
                    # with open(error_file, 'a') as q:
                    #     q.write(f'[!] Value of key "value":[{data["nfts"][j]["metadata"]["attributes"][smt]["value"]}]'
                    #             f'from tag:{tag} has incorrect syntax'"\n")
                    #     q.close()
                    check_attr.append(f'[!] Value of key "value":'
                                      f'[{data["nfts"][j]["metadata"]["attributes"][smt]["value"]}]'
                                      f' from tag:{tag} has incorrect syntax')
                    second_check = False
                for var in data["nfts"][j]["metadata"]["attributes"][smt]['value'].split():
                    var_1 = ''.join([c for c in var if c.isupper()])
                    if len(var_1) > 1 and not var.isupper():
                        if '-' in var and len(var_1) == len(var.split('-')):
                            continue
                        second_check = False
                        print(f'[!] (Value) key: [{data["nfts"][j]["metadata"]["attributes"][smt]["value"]}]'
                              f' from (attributes), has incorrect syntax in tag: {tag}')
                        check_attr.append(f'[!] (Value) key: '
                                          f'[{data["nfts"][j]["metadata"]["attributes"][smt]["value"]}]'
                                          f' from (attributes), has incorrect syntax in tag: {tag}')
                        # with open(outer_file, 'a') as f:
                        #     f.write(
                        #         "\n"f'[!] (Value) key: [{data["nfts"][j]["metadata"]["attributes"][smt]["value"]}]'
                        #         f' from (attributes), has incorrect syntax in tag: {tag}'"\n")
                        #     f.close()
                        # with open(error_file, 'a') as q:
                        #     q.write(
                        #         "\n"f'[!] (Value) key: [{data["nfts"][j]["metadata"]["attributes"][smt]["value"]}]'
                        #         f' from (attributes), has incorrect syntax in tag: {tag}'"\n")
                        #     q.close()
        else:
            print("[!] EMPTY key 'attributes' check above message(s)")
            # with open(outer_file, 'a') as f:
            #     f.write(f'[!] EMPTY key "attributes" check above message(s)'"\n")
            #     f.close()
            # with open(error_file, 'a') as q:
            #     q.write(f'[!] EMPTY key "attributes" check above message(s)'"\n")
            #     q.close()
            check_attr.append("[!] EMPTY key 'attributes' check above message(s)")
            second_check = False
    if first_check and second_check:
        print("[v] OK")
        # with open(outer_file, 'a') as f:
        #    f.write("[v] OK""\n")
        #    f.close()
        # with open(error_file, 'a') as q:
        #    q.write(f'[v] No errors exist''\n')
        #    q.close()
        check_attr.append(f'[v] No errors exist')
    with open(error_file, 'w') as fp:
        fp.write((2*'\n').join(check_attr))
    return error_file


def check_unique_links(data_1):
    file_format = os.path.basename(data_1).split('.')[-1]
    if file_format != 'json':
        check_format = 'Json filename(filepath) is incorrect'
        return check_format
    # else:
    #    check_format = 'Json filename is correct start checking...'
    try:
        with open(data_1, encoding='UTF8') as file:
            data = json.load(file)
    except Exception as smth:
        print(smth)
        exit()
    now = datetime.datetime.now()
    times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
    current_time = '_'.join(times[1].split(':'))
    current_date = '_'.join(times[0].split("-"))
    filename = 'link_uniqueness_check_results_' + current_date + '_' + current_time + '_.txt'
    error_file = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\' + filename
    check_url_un = []
    print('\n'"[*] CHECKING IF URLS ARE UNIQUE.....")
    # with open(outer_file, 'a') as f:
    #    f.write('\n'f'[*] CHECKING IF URLS ARE UNIQUE.....''\n')
    # with open(error_file, 'w') as q:
    #     q.write('\n'f'[*] CHECKING IF URLS ARE UNIQUE.....''\n')
    check_url_un.append(f'[*] CHECKING IF URLS ARE UNIQUE.....')
    check_2 = True
    check_3 = True
    list_url = []
    for i in range(len(data["nfts"])):
        if 'animation_url' in list(data['nfts'][i]['metadata'].keys()):
            an_url = data["nfts"][i]["metadata"]["animation_url"]
            if an_url not in list_url:
                list_url.append(an_url)
            else:
                check_2 = False
                # with open(outer_file, 'a') as f:
                #    f.write('\n'f'[!] {an_url} [is NOT unique]''\n')
                print('\n'f'[!] {an_url} [is NOT unique]''\n')
                # with open(error_file, 'a') as q:
                #    q.write(f'[!] {an_url} [is NOT unique]''\n')
                check_url_un.append(f'[!] {an_url} [is NOT unique]')
        else:
            check_2 = False
            print('[!] There is(are) EMPTY "animation_url" key,check message(s) from key check at the beginning')
            #with open(outer_file, 'a') as f:
            #    f.write(f'[!] There is(are) EMPTY "animation_url" key,check message(s) from key check at the beginning'
            #            '\n')
            # with open(error_file, 'a') as q:
            #    q.write(f'[!] There is(are) EMPTY "animation_url" key,check message(s) from key check at the beginning'
            #            '\n')
            check_url_un.append(f'[!] There is(are) EMPTY "animation_url" key,check message(s) '
                                f'from key check at the beginning')
        if 'image' in list(data['nfts'][i]['metadata'].keys()):
            img_url = data["nfts"][i]["metadata"]["image"]
            if img_url not in list_url:
                list_url.append(img_url)
            else:
                check_3 = False
                # with open(outer_file, 'a') as f:
                #    f.write('\n'f'[!] {img_url} [is NOT UNIQUE]''\n''\n')
                print('\n'f'[!] {img_url} [is not UNIQUE]''\n')
                # with open(error_file, 'a') as q:
                #     q.write(f'[!] {img_url} [is NOT UNIQUE]''\n')
                check_url_un.append(f'[!] {img_url} [is NOT UNIQUE]')
        else:
            check_3 = False
            print('[!] There is(are) EMPTY "image" key,check message(s) from key check at the beginning')
            # with open(outer_file, 'a') as f:
            #    f.write(f'[!] There is(are) EMPTY "image" key,check message(s) from key check at the beginning''\n')
            # with open(error_file, 'a') as q:
            #    q.write(f'[!] There is(are) EMPTY "image" key,check message(s) from key check at the beginning''\n')
            check_url_un.append(f'[!] There is(are) EMPTY "image" key,check message(s) from key check at the beginning')
    if check_2 and check_3:
        print("[v] CHECK OVER ALL URLS ARE UNIQUE")
        # with open(outer_file, 'a') as f:
        #    f.write(f'[v] CHECK OVER ALL URLS ARE UNIQUE''\n')
        # with open(error_file, 'a') as q:
        #    q.write(f'[v] No errors exist''\n')
        check_url_un.append(f'[v] No errors exist')
    else:
        print("[v] CHECK OVER")
        #with open(outer_file, 'a') as f:
        #    f.write(f'[v] CHECK OVER''\n')
    with open(error_file, 'w') as fp:
        fp.write((2*'\n').join(check_url_un))
    return error_file


def check_unique_tags(data_1):
    file_format = os.path.basename(data_1).split('.')[-1]
    if file_format != 'json':
        check_format = 'Json filename(filepath) is incorrect'
        return check_format
    # else:
    #    check_format = 'Json filename is correct start checking...'
    try:
        with open(data_1, encoding='UTF8') as file:
            data = json.load(file)
    except Exception as smth:
        print(smth)
        exit()
    now = datetime.datetime.now()
    times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
    current_time = '_'.join(times[1].split(':'))
    current_date = '_'.join(times[0].split("-"))
    filename = 'tag_uniqueness_check_results_' + current_date + '_' + current_time + '_.txt'
    error_file = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\' + filename
    check_tag_un = []
    print('\n'"[*] CHECKING IF TAGS ARE UNIQUE.....")
    check_tag_un.append("[*] CHECKING IF TAGS ARE UNIQUE.....")
    #with open(outer_file, 'a') as f:
    #    f.write('\n'f'[*] CHECKING IF TAGS ARE UNIQUE.....''\n')
    # with open(error_file, 'w') as q:
    #    q.write('\n'f'[*] CHECKING IF TAGS ARE UNIQUE.....''\n')
    list_tag = []
    check_1 = True
    for i in range(len(data["nfts"])):
        if 'tag' in list(data['nfts'][i].keys()):
            tag = data['nfts'][i]['tag']
            if tag not in list_tag:
                list_tag.append(tag)
            else:
                check_1 = False
                #with open(outer_file, 'a') as f:
                #    f.write(f'[!] tag: {tag} [is NOT UNIQUE]''\n')
                print(f'[!] tag: {tag} [is not UNIQUE]''\n')
                # with open(error_file, 'a') as q:
                #    q.write(f'[!] tag: {tag} [is NOT UNIQUE]''\n')
                check_tag_un.append(f'[!] tag: {tag} [is NOT UNIQUE]')
        else:
            print('[!] There is(are) EMPTY "tag" key,check message(s) from key check at the beginning')
            # with open(outer_file, 'a') as f:
            #    f.write(f'[!] There is(are) EMPTY "tag" key,check message(s) from key check at the beginning''\n')
            # with open(error_file, 'a') as q:
            #    q.write(f'[!] There is(are) EMPTY "tag" key,check message(s) from key check at the beginning''\n')
            check_tag_un.append(f'[!] There is(are) EMPTY "tag" key,check message(s) from key check at the beginning')
            check_1 = False
    if check_1:
        print("[v] CHECK OVER TAGS ARE UNIQUE")
        # with open(outer_file, 'a') as f:
        #    f.write(f'[v] CHECK TAGS ARE UNIQUE''\n')
        # with open(error_file, 'a') as q:
        #    q.write(f'[v] No errors exist''\n')
        check_tag_un.append(f'[v] No errors exist')
    else:
        print("[v] CHECK OVER")
        #with open(outer_file, 'a') as f:
        #    f.write(f'[v] CHECK OVER''\n')
    with open(error_file, 'w') as fp:
        fp.write((2*'\n').join(check_tag_un))
    return error_file

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


def get_image_link(data_1):
    file_format = os.path.basename(data_1).split('.')[-1]
    if file_format != 'json':
        check_format = 'Json filename(filepath) is incorrect'
        return check_format
    # else:
    #    check_format = 'Json filename is correct start checking...'
    try:
        with open(data_1, encoding='UTF8') as file:
            data = json.load(file)
    except Exception as smth:
        print(smth)
        exit()
    error_file = 'C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\image_resolution_check_results.txt'
    error = 0
    check_im_link = []
    print("\n"f"[*] CHECKING IMAGE SIZE({width_images}x{height_images}).....")
    check_im_link.append(f"[*] CHECKING IMAGE SIZE({width_images}x{height_images}).....")
    # with open(outer_file, 'a') as f:
    #    f.write("\n"f'[*] CHECKING IMAGE SIZE({width_images}x{height_images})... ''\n')
    # with open(error_file, 'a') as q:
    #    q.write("\n"f'[*] CHECKING IMAGE SIZE({width_images}x{height_images})... ''\n')
    check_1 = True
    for i in range(len(data["nfts"])):
        if 'image' in list(data["nfts"][i]["metadata"].keys()):
            # noinspection PyBroadException
            try:
                uri = data["nfts"][i]["metadata"]["image"]
                if uri.split('.')[-1] == type_to_check:
                    print("\n"f'[!] {uri} [This is not an image url]'"\n")
                    # with open(outer_file, 'a') as f:
                    #    f.write("\n"f'[!] {uri} [This is not an image url]'"\n""\n")
                    # with open(error_file, 'a') as q:
                    #    q.write(f'[!] {uri} [This is not an image url]'"\n")
                    check_im_link.append(f'[!] {uri} [This is not an image url]')
                    continue
                width, height = get_sizes(uri)
                if width != width_images or height != height_images:
                    print('\n''[!]', uri, " [size should be 1500x1500 but it is ]"'\n')
                    # with open(outer_file, 'a') as f:
                    #    f.write('\n'f'[!] {uri} , [size should be 1500x1500, but it is {width}x{height} ]''\n''\n')
                    # with open(error_file, 'a') as q:
                    #    q.write(f'[!] {uri} , [size should be 1500x1500, but it is {width}x{height}]''\n')
                    check_im_link.append(f'[!] {uri} , [size should be 1500x1500, but it is {width}x{height} ]')
                    check_1 = False
                else:
                    print('[v] ', uri, " [OK]")
                    #with open(outer_file, 'a') as f:
                    #    f.write(f'[v] {uri} , [OK]'"\n")
                    check_im_link.append(f'[v] {uri} , [OK]')
            except:
                error += 1
                print(f'[!] this is an incorrect link')
                #with open(outer_file, 'a') as f:
                #    f.write(f'[!] this is an incorrect link'"\n")
                #with open(error_file, 'a') as q:
                #    q.write(f'[!] this is an incorrect link'"\n")
                check_im_link.append(f'[!] this is an incorrect link')
        else:
            #with open(outer_file, 'a') as f:
            #    f.write(f'[!] There is(are) EMTPY "image" key check above message(s)'"\n")
            print(f'[!] There is(are) EMTPY "image" key check message(s) above')
            #with open(error_file, 'a') as q:
            #    q.write(f'[!] There is(are) EMTPY "image" key check above message(s)'"\n")
            check_im_link.append(f'[!] There is(are) EMTPY "image" key check above message(s)')
        if not check_1:
            error += 1
    if error == 0:
        print("[v] IMAGE SIZE CHECK ENDS,ALL IMAGES ARE IN CORRECT SIZE")
        #with open(outer_file, 'a') as f:
        #    f.write(f'[v] IMAGE SIZE CHECK ENDS,ALL IMAGES ARE IN CORRECT SIZE'"\n")
        # with open(error_file, 'a') as q:
        #    q.write(f'[v] No errors exist''\n')
        check_im_link.append(f'[v] No errors exist')
    with open(error_file, 'w') as fp:
        fp.write((2*'\n').join(check_im_link))



#if __name__ == '__main__':
# parser = argparse.ArgumentParser()
# parser.add_argument('-json', help="json file path to check", required=True)
# args = parser.parse_args()
# json_path = args.json
# for smth in os.listdir(os.getcwd()):
#     if smth.endswith('.json'):
#         json_path = smth
#                             ####VARIABLES######
########################################################################################
config_path = os.path.join(os.environ["USERPROFILE"], 'Desktop', 'script_config.ini')
read_config = configparser.RawConfigParser()
read_config.read(config_path)
width_videos = int(read_config.get("Variable Section for test_json", "width_videos"))
height_videos = int(read_config.get("Variable Section for test_json", "height_videos"))
width_images = int(read_config.get("Variable Section for test_json", "width_images"))
height_images = int(read_config.get("Variable Section for test_json", "height_images"))
type_to_check = read_config.get("Variable Section for test_json", "type_to_check")
########################################################################################
now = datetime.datetime.now()
times = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
current_time = '_'.join(times[1].split(':'))
current_date = '_'.join(times[0].split("-"))
# base_path = os.path.join(os.environ["USERPROFILE"], 'Desktop', 'test_json_outputs')
# if not os.path.exists(base_path):
#     os.mkdir(base_path)
# outer_filename = 'tested_at-' + current_date + '_' + current_time + '.txt'
# error_filename = 'errors_at-' + current_date + '_' + current_time + '.txt'
# outer_file = os.path.join(base_path, outer_filename)
# error_file = os.path.join(base_path, error_filename)
# noinspection PyBroadException
# try:
#     with open(json_path, encoding='UTF8') as file:
#         jsonData = json.load(file)
# except Exception as smth:
#     print("json filename(filepath) is incorrect")
#     exit()
# check_keys(jsonData)
# check_values(jsonData)
# check_tag_domain_last_digits(jsonData)
# check_syntax(jsonData)
# calculate_arguments(jsonData)
# check_unique_links(jsonData)
# check_unique_tags(jsonData)
# check_animation_urls(jsonData)
# check_image_urls(jsonData)
# get_image_link(jsonData)
# checking_videos_resolution(jsonData)
