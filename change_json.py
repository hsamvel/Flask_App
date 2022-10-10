import json


def write_json(new_data, smth, filename):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside nfts
        # print(file_data["nfts"][int(smth)])
        if "COMMENTS" in file_data["nfts"][smth].keys():
            new_data["COMMENTS"] += ", " + file_data["nfts"][smth]["COMMENTS"]
            file_data["nfts"][smth].update(new_data)
        else:
            file_data["nfts"][smth].update(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)

    # python object to be appended

