import json


def get_index(im, json_file_path):
    with open(json_file_path, encoding='UTF8') as file:
        data = json.load(file)
    for i in range(len(data["nfts"])):
        val = i
        if data["nfts"][i]["metadata"]["image_url"] == im:
            return int(val)


def get_index_from_vid(im, json_file_path):
    with open(json_file_path, encoding='UTF8') as file:
        data = json.load(file)
    for i in range(len(data["nfts"])):
        val = i
        if data["nfts"][i]["metadata"]["animation_url"] == im:
            return int(val)
