import time
from base_camera import BaseCamera
from webParts import app
import os


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    # imgs = [open('D:\charm_project\\flask-video-streaming\\' + f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
    imgs = os.listdir(app.config['UPLOAD_FOLDER'])

    def reset_frames(self):
        count = 0
        for _ in self.imgs:
            if count == 3:
                break
            os.remove(_)
            count += 1
        self.imgs = os.listdir(app.config['UPLOAD_FOLDER'])

    @classmethod
    def frames(cls):
        count = 0
        while True:
            # time.sleep(0.1)
            if count == 3:
                cls.reset_frames()
            yield Camera.imgs[int(time.time()) % 3]
            count += 1
