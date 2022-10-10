import urllib.request
import csv


def check_link(csv_links):
    with open(csv_links, encoding='UTF8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_reader_list = list(csv_reader)
    new_list = []
    for i in range(len(csv_reader_list)):
        for key in csv_reader_list[i]:
            try:
                urllib.request.urlopen(csv_reader_list[i][key]).getcode()
                new_list.append(f"[*] {csv_reader_list[i][key]} [OK]")
            except:
                new_list.append(f"[!] {csv_reader_list[i][key]} [INCORRECT]")
    text_file = 'check_results.txt'
    textfile = open(text_file, "w")
    for element in new_list:
        textfile.write(element + "\n")
    textfile.close()
    return text_file
