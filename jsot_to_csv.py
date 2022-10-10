import json
import pandas as pd


# First loading Json data into a dictionary.
def json_csv_conv(filename):
    with open(filename, 'r+') as file:
        file_data = json.load(file)

    # Creating dictionary with Json file keys(all keys are empty python lists).
    dict_whole = {}
    for el in file_data["nfts"][0]:
        if el != "metadata":
            dict_whole[el] = []
        if el == "metadata":
            for elem in file_data["nfts"][0]["metadata"]:
                if elem != "attributes":
                    dict_whole[elem] = []


# Get all key names of attributes.
    attributes = []
    for i in range(len(file_data["nfts"])):
        for j in range(len(file_data["nfts"][i]["metadata"]["attributes"])):
            # Checking whether key is on attributes(python list) or not, If not adding.
            if file_data["nfts"][i]["metadata"]["attributes"][j]["trait_type"] + "_attr" not in list(dict_whole.keys()):
                dict_whole[file_data["nfts"][i]["metadata"]["attributes"][j]["trait_type"] + "_attr"] = []
                attributes.append(file_data["nfts"][i]["metadata"]["attributes"][j]["trait_type"] + "_attr")


# Writing values of each key section by section to dict_whole(python dictionary).
    count = 1
    for i in range(len(file_data["nfts"])):
        # Writing metadata values.
        count = 1
        new_attr = []
        dict_whole["tag"].append(file_data["nfts"][i]['tag'])
        dict_whole["domain"].append(file_data["nfts"][i]['domain'])
        dict_whole['animation_url'].append(file_data["nfts"][i]['metadata']["animation_url"])
        dict_whole['image_url'].append(file_data["nfts"][i]['metadata']["image_url"])
        dict_whole['description'].append(file_data["nfts"][i]['metadata']["description"])
        dict_whole['name'].append(file_data["nfts"][i]['metadata']["name"])
        # Writing attribute values.
        for k in range(len(file_data["nfts"][i]["metadata"]["attributes"])):
            count += 1
            dict_whole[file_data["nfts"][i]["metadata"]["attributes"][k]["trait_type"] + "_attr"].append(
                file_data["nfts"][i]["metadata"]["attributes"][k]["value"])
            # If attribute key does not exist in this section adding <None> for value of that attribute key.
            new_attr.append(file_data["nfts"][i]["metadata"]["attributes"][k]["trait_type"] + "_attr")
            if count == len(file_data["nfts"][i]["metadata"]["attributes"]) + 1:
                for eq in attributes:
                    if eq not in new_attr:
                        dict_whole[eq].append("None")


# Writing dict_whole(python dictionary) into csv file in required format with the help of pandas(python library).
    df = pd.DataFrame.from_dict(dict_whole)
    file_full_path = "C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\test_new__811.csv"
    df.to_csv(file_full_path, index=False, header=True)
    return file_full_path



