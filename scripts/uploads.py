import os
import time
import requests

# print(os.pardir)
# print(os.path.dirname(__file__))
# print(os.path.abspath())
UPLOAD_PATH = "/var/lib/motion/"
# UPLOAD_URL = "118.25.42.123/upload"
UPLOAD_URL = "http://118.25.42.123:5000/upload"


def combine_params(dif: list):
    results = [('files', open(UPLOAD_PATH + file, "rb")) for file in dif]
    return results


while True:
    current_files = os.listdir(UPLOAD_PATH)
    time.sleep(1)
    second_after = os.listdir(UPLOAD_PATH)
    difference = list(set(current_files).difference(set(second_after)))
    # print(difference)

    images = combine_params(difference)

    response = requests.post(UPLOAD_URL, files=images)
    # print(response.text)

#
# while True:
#     difference = ['1.jpg', '2.jpg', '3.jpg']
#     # images = combine_params(difference)
#     # print(images)
#     images = [('images', open('1.jpg', 'rb')),
#               ('images', open('2.jpg', 'rb')),
#               ('images', open('3.jpg', 'rb'))]
#     # print(images)
#     response = requests.post(UPLOAD_URL, files=images)
#     # time.sleep(3)
#     time.sleep(1)