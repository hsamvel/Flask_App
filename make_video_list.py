import json
import os.path
import pandas as pd
import urllib.request
from PIL import Image
global list_for_preview, new_list, new_list_1


def links_to_dict(data):
    new_dict = {}
    list_a = []
    with open(data, encoding='UTF8') as file:
        data = json.load(file)
    for i in range(len(data["nfts"])):
        for el in data["nfts"][i]["metadata"]["attributes"]:
            new_dict[el['trait_type']] = el['value']
        f = pd.DataFrame(new_dict.items(), columns=["Trait_Type", "Value"])
        html = f.to_html()
        list_a.append(html)
        new_dict = {}
    new_lst = []
    for el in list_a:
        new_el = f'<div style= "display: inline-block;">{el}</div>'
        new_lst.append(new_el)
    return new_lst


def links_to_list(data): #+
    with open(data, encoding='UTF8') as file:
        data = json.load(file)
    video_link_list = []
    for i in range(len(data["nfts"])):
        id_a = f'a_{i}'
        video_link_list.append(f'<video width="390" height="390" '
                               f'controls src={data["nfts"][i]["metadata"]["animation_url"]} preload="none"></video>'
                               f'<a class=smth id={id_a} ' 
                               f' onclick="openNav(\'{id_a}\')"  href="#?vid={data["nfts"][i]["metadata"]["animation_url"]}"'
                               f'style="position: absolute;">Send Report</a>')
    return video_link_list


def links_to_list_3(data): #+
    with open(data, encoding='UTF8') as file:
        data = json.load(file)
    video_link_list = []
    for i in range(len(data["nfts"])):
        video_link_list.append(f'<video width="390" height="390" '
                               f'controls src={data["nfts"][i]["metadata"]["animation_url"]} preload="none"></video>'
                               )
    return video_link_list


def links_to_list_vidim(data, spec_attr): # -
    with open(data, encoding='UTF8') as file:
        data = json.load(file)
        global list_for_preview
        list_for_preview = []
        video_link_list = []
        keys = list(spec_attr)
    for i in range(len(data["nfts"])):
        for el in spec_attr:
            for j in range(len(data["nfts"][i]["metadata"]["attributes"])):
                if data["nfts"][i]["metadata"]["attributes"][j]['value'] in spec_attr[el] and \
                        "".join(data["nfts"][i]["metadata"]["attributes"][j]['trait_type'].split()) == el:
                    list_for_preview.append(int(i))
    global new_list
    new_list = []
    for smth in list_for_preview:
        if list_for_preview.count(smth) == len(keys) and smth not in new_list:
            new_list.append(smth)
    for elem in new_list:
        video_link_list.append(f'<video width="390" height="390" controls '
                               f'src={data["nfts"][elem]["metadata"]["animation_url"]} preload="none"></video>'
                               )
    return video_link_list


def links_to_list_new(data, spec_attr): # +
    with open(data, encoding='UTF8') as file:
        data = json.load(file)
        global list_for_preview
        list_for_preview = []
        video_link_list = []
        keys = list(spec_attr)
    for i in range(len(data["nfts"])):
        for el in spec_attr:
            for j in range(len(data["nfts"][i]["metadata"]["attributes"])):
                if data["nfts"][i]["metadata"]["attributes"][j]['value'] in spec_attr[el] and \
                        "".join(data["nfts"][i]["metadata"]["attributes"][j]['trait_type'].split()) == el:
                    list_for_preview.append(int(i))
    global new_list
    new_list = []
    for smth in list_for_preview:
        if list_for_preview.count(smth) == len(keys) and smth not in new_list:
            new_list.append(smth)
    count = 0
    for elem in new_list:
        count += 1
        id_a = f'a_{count}'
        video_link_list.append(f'<video width="390" height="390" controls '
                               f'src={data["nfts"][elem]["metadata"]["animation_url"]} preload="none"></video>'
                               f'<a class=smth id={id_a} '
                               f' onclick="openNav(\'{id_a}\')"  href="#?vid={data["nfts"][elem]["metadata"]["animation_url"]}"'
                               f'style="position: absolute;">Send Report</a>'
                               )
    return video_link_list


def links_to_dict_new(data): # +
    new_dict = {}
    list_a = []
    with open(data, encoding='UTF8') as file:
        data = json.load(file)
    for elem in new_list:
        for el in data["nfts"][elem]["metadata"]["attributes"]:
            new_dict[el['trait_type']] = el['value']
        f = pd.DataFrame(new_dict.items(), columns=["Trait_Type", "Value"])
        html = f.to_html()
        list_a.append(html)
        new_dict = {}
        new_el = ""
    new_lst = []
    for el in list_a:
        new_el = f'<div style= "display: inline-block;">{el}</div>'
        new_lst.append(new_el)
    return new_lst


# This function finds and appends all image links from json file into python list and used for (preview images)
def links_to_list_1(data): # +
    # First we load json file to python dictionary
    with open(data, encoding='UTF8') as file:
        data = json.load(file)
    global image_link_list
    image_link_list = []
    # Appending each image link to python list in html required format
    for i in range(len(data["nfts"])):
        id = f"img_{i}"
        id_a = f"a_{i}"
        image_link_list.append(f'<a href="/preview-55?image={data["nfts"][i]["metadata"]["image_url"]}" '
                               f'target="_blank"> <img id={id} class="img" onerror="this.onerror=null; '
                               f'this.src=\'/static/images/Empty link_390x390.png\'" '
                               f'src="{data["nfts"][i]["metadata"]["image_url"]}" style="width:390px;height:390px;" '
                               f'loading=lazy > </a> <a class=smth id={id_a} ' 
                               f' onclick="openNav(\'{id_a}\')"  href="#?img={data["nfts"][i]["metadata"]["image_url"]}"'
                               f'style="position: absolute;">Send Report</a>')
    return image_link_list


def links_to_list_1_new(data, spec_attr): #+
    with open(data, encoding='UTF8') as file:
        data = json.load(file)
    global list_for_preview
    list_for_preview = []
    image_link_list = []
    keys = list(spec_attr)
    for i in range(len(data["nfts"])):
        for el in spec_attr:
            for j in range(len(data["nfts"][i]["metadata"]["attributes"])):
                if data["nfts"][i]["metadata"]["attributes"][j]['value'] in spec_attr[el] and \
                        "".join(data["nfts"][i]["metadata"]["attributes"][j]['trait_type'].split()) == el:
                    list_for_preview.append(int(i))
    global new_list_1
    new_list_1 = []
    for smth in list_for_preview:
        if list_for_preview.count(smth) == len(keys) and smth not in new_list_1:
            new_list_1.append(smth)
    for element in new_list_1:
        image_link_list.append(f' <a href="{data["nfts"][element]["metadata"]["image_url"]}" target="_blank">'
                               f' <img class="img" onerror="this.onerror=null; '
                               f'this.src=\'/static/images/Empty link_390x390.png\'" '
                               f'src="{data["nfts"][element]["metadata"]["image_url"]}"'
                               f'  style="width:390px;height:390px;" loading=lazy alt=""/> '
                               f'</a> <a class=smth'
                               f' onclick="openNav()"  href="#?img={data["nfts"][element]["metadata"]["image_url"]}"'
                               f'style="position: absolute;">Send Report</a>')
    return image_link_list


def links_to_dict_new_img(data): # +
    new_dict = {}
    list_a = []
    with open(data, encoding='UTF8') as file:
        data = json.load(file)
    for elem in new_list_1:
        for el in data["nfts"][elem]["metadata"]["attributes"]:
            new_dict[el['trait_type']] = el['value']
        f = pd.DataFrame(new_dict.items(), columns=["Trait_Type", "Value"])
        html = f.to_html()
        list_a.append(html)
        new_dict = {}
    new_lst = []
    for el in list_a:
        new_el = f'<div style= "display: inline-block;">{el}</div>'
        new_lst.append(new_el)
    return new_lst


def down_img(url):
    img_name = url.split("/")[-1]
    urllib.request.urlretrieve(url, img_name)
    im1 = Image.open(img_name)
    im2 = Image.open("Grid.png")
    im1.paste(im2, (0, 0), mask=im2)
    im1.save('im_grid.png')
    im_path = os.path.abspath("im_grid.png")
    print(im_path)
    return im_path


# This function create html objects with image links from data and appends it to new_im_link_list(python list)
# We use this for (preview images and videos)
def links_to_list_vid_im(data): #+
    # First we load json file to python dictionary
    with open(data, encoding='UTF8') as file:
        data = json.load(file)
    new_im_link_list = []
    # Finding image links from loaded json and appending them into python list in html required format
    for i in range(len(data["nfts"])):
        # id_1 is unique id for each html <img> objects
        id_1 = f"img_{i}"
        new_im_link_list.append(f'<a href="/preview-55?image={data["nfts"][i]["metadata"]["image_url"]}" '
                                f'target="_blank">'
                                f'<img src="{data["nfts"][i]["metadata"]["image_url"]}" id={id_1} '
                                f'style="width:390px;height:390px;"><a><a class=smth onclick="openNav()" '
                                f'href="#?image={data["nfts"][i]["metadata"]["image_url"]}";  '
                                f'style="position: absolute;">Send Report</a>')
    # function returns python list which includes all image links from json file
    return new_im_link_list
