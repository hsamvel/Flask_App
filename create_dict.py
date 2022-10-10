import json
from flask import jsonify



def attrs_to_dict(data):
    with open(data, encoding='UTF8') as file:
        data = json.load(file)
    new_dict = {}
    list_a = []
    count = 0
    full_data = {}
    for i in range(len(data["nfts"])):
        for el in data["nfts"][i]["metadata"]["attributes"]:
            if ''.join(el['trait_type'].split()) not in list(new_dict.keys()):
                new_dict[''.join(el['trait_type'].split())] = [el['value']]
            else:
                if el['value'] not in new_dict[''.join(el['trait_type'].split())]:
                    new_dict[''.join(el['trait_type'].split())].append(el['value'])
    full_data["Attributes"] = {}
    full_data["Attributes"] = new_dict
    #print(json.dumps(full_data,indent=4))
    return json.dumps(full_data,indent=4)



#attrs_to_dict("C:\\Users\\Neo Graph Games\\Downloads\\generated_at-11_07_2022_12_21_59_52845259.json")

