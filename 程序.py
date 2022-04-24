# Untitled - By: 86731 - 周三 3月 24 2021

import sensor, image, time
import json
from pyb import Servo
from pyb import UART


bule_threshold  = (76, 27, -28, -8, -33, -5)

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # use RGB565.
sensor.set_framesize(sensor.QQVGA) # use QQVGA for speed.
sensor.skip_frames(10) # Let new settings take affect.
sensor.set_auto_whitebal(False) # turn this off.
#sensor.set_vflip(True)
clock = time.clock() # Tracks FPS.
uart = UART(3, 9600)

def find_max(blobs):
    max_pixels=0
    for blob in blobs:
        if blob[4] > max_pixels:
            max_blob=blob
            max_pixels = blob[4]
    return max_blob

while(True):
    clock.tick() # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot() # Take a picture and return the image.

    blobs = img.find_blobs([bule_threshold],pixels_threshold=200, area_threshold=200, merge=True)
    if blobs:
        max_blob = find_max(blobs)
        img.draw_rectangle(max_blob.rect()) # rect
        img.draw_cross(max_blob.cx(), max_blob.cy()) # cx, cy
        pcx=max_blob.cx()
        pcy=max_blob.cy()
        data={
        "cx":pcx,
        "cy":pcy}

        data_out = json.dumps(data)
        uart.write(data_out +'\n')
        print('you send:',data_out)
    else:
        print("not found!")
