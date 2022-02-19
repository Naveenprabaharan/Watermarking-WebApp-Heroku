import cv2
from PIL import Image
import numpy as np
import base64
import io


def Water_Mark(Water_Mark_image, Water_Mark_Text, Water_Mark_Position, Water_Mark_Text_size):
    path = Water_Mark_image
    image = Image.open(Water_Mark_image)

    # Reading an image in default mode
    frame = np.array(image, dtype="uint8")

    # Window name in which image is displayed
    window_name = 'Image'

    # font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # org
    watermarksize = image.size
    if (Water_Mark_Position == 'Top Right'):
        x = int((watermarksize[0] * 0.60))
        y = int(watermarksize[1] - (watermarksize[1] * 0.90))

    elif (Water_Mark_Position == 'Top Left'):
        x = int(watermarksize[0] - (watermarksize[0] * 0.90))
        y = int(watermarksize[1] - (watermarksize[1] * 0.90))
    elif (Water_Mark_Position == 'Bottom Right'):
        x = int((watermarksize[0] * 0.60))
        y = int((watermarksize[1] * 0.9))
    elif (Water_Mark_Position == 'Bottom Left'):
        x = int(watermarksize[0] - (watermarksize[0] * 0.90))
        y = int((watermarksize[1] * 0.9))
    else:
        x = int(watermarksize[0] / 2)
        y = int((watermarksize[1] / 2))
    org = (x, y)

    # fontScale
    fontScale = 1

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    # Using cv2.putText() method
    image = cv2.putText(frame, Water_Mark_Text, org, font, fontScale, color, thickness, cv2.LINE_AA)
    image = Image.fromarray(image)
    data = io.BytesIO()

    image.save(data, format="png")
    encoded_img_data = base64.b64encode(data.getvalue())

    return encoded_img_data
