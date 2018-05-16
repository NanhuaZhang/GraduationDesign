import time
from base_camera import BaseCamera
import os
folder = 'static/uploads/videoFrames'


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    # imgs = [open('D:\charm_project\\flask-video-streaming\\' + f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
    # imgs = os.listdir(app.config['UPLOAD_FOLDER'])

    @staticmethod
    def frames():
        count = 0
        while True:
            # time.sleep(0.1)
            frame = os.listdir(folder)[0]
            yield frame
            os.remove(os.path.join(folder, frame))
