import time
from base_camera import BaseCamera
import os
import random
folder = 'static/uploads/videoFrames/'


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    # imgs = [open('D:\charm_project\\flask-video-streaming\\' + f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
    # imgs = os.listdir(app.config['UPLOAD_FOLDER'])

    @staticmethod
    def frames():
        time.sleep(3)
        while True:
            # time.sleep(0.1)
            # print("before" + str(time.time()))
            current_frames = os.listdir(folder)
            print(current_frames)
            try:
                yield open(current_frames[0], 'rb').read()
                os.remove(folder + current_frames[0])
                print(current_frames)
            except IndexError:
                yield open("static/uploads/error/timg.jpg", 'rb').read()
            # print("after" + str(time.time()))

