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
            if len(os.listdir(folder)) == 1:
                yield open(folder + 'timg.jpg', 'rb').read()
                continue
            current_frames = os.listdir(folder)
            # 每秒10帧
            time.sleep(0.1)
            start = current_frames[0]
            print(start)
            yield open(folder + start, 'rb').read()
            if len(os.listdir(folder)) > 1:
                os.remove(folder + start)

