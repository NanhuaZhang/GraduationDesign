import os
import time
import requests

# print(os.pardir)
# print(os.path.dirname(__file__))
# print(os.path.abspath())
UPLOAD_PATH = os.path.dirname(__file__)
# UPLOAD_URL = "118.25.42.123/upload"
UPLOAD_URL = "http://127.0.0.1:5000/upload"


def combine_params(dif: list):
    results = [(file.split('.')[0], open(UPLOAD_PATH + file, "wb")) for file in dif]
    return results

#
# while True:
#     current_files = os.listdir(UPLOAD_PATH)
#     time.sleep(1)
#     second_after = os.listdir(UPLOAD_PATH)
#     difference = list(set(current_files).difference(set(second_after)))
#     print(difference)
#
#     files["fields"] = combine_params(difference)
#
#     response = requests.post(UPLOAD_URL, files=files)
#     print(response.text)
    # print("upload failure")


while True:
    difference = ['1.jpg', '2.jpg', '3.jpg']
    # images = combine_params(difference)
    # print(images)
    images = [('images', open('1.jpg', 'rb')),
              ('images', open('2.jpg', 'rb')),
              ('images', open('3.jpg', 'rb'))]
    # print(images)
    response = requests.post(UPLOAD_URL, files=images)
    print(response.text)
    time.sleep(60)
