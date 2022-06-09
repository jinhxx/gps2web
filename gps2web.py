#!/usr/bin/env python
from sys import flags
from selenium import webdriver
from serial import Serial
from time import sleep
from haversine import haversine
from time import time
import cv2

# latitude  = 36.520110249349656
# longitude = 127.173039246793640
latitude  = 36.609820
longitude = 127.284303
center = (36.609820, 127.284303)
dist = 0.0
t1 = t2 = 0.0
flag = False

# OFFSET_LAT = -13.645105
# OFFSET_LON = 126.715070
ser = Serial('/dev/ttyACM0',9600)
# ser = Serial('/dev/ttyACM0',115200)
drv = webdriver.Chrome(executable_path="/home/jino/chromedriver_linux64/chromedriver")

def show_img():
    img = cv2.imread('push.jpg', cv2.IMREAD_COLOR)
    down_width = 427
    down_height = 613
    down_points = (down_width, down_height)
    resized_down = cv2.resize(img, down_points, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('image', resized_down)
    cv2.waitKey(0)
    cv2.destroyWindow('image')

drv.get('http://localhost:8080')

while True:
    #drv.get('http://localhost:8080
    if ser.readable():
        res = ser.readline()       
        try:
            if(res.decode()[0:3]) == 'lat':
                latitude = float(res.decode()[3:12])
                # print("위도:", latitude)
            if(res.decode()[12:15]) == 'lon':
                longitude = float(res.decode()[15:])
                # print("경도:", longitude)
        except ValueError as e:
            continue
        
        pos = (latitude, longitude)
        dist = haversine(center, pos) * 1000
        print(f"위도: {latitude}, 경도: {longitude}, 거리: {int(dist)}m")

        # drv.execute_script("update_gps(%s, %s)" %(str(latitude), str(longitude)))
        drv.execute_script("update_gps(%s, %s)" %(str(latitude), str(longitude)))

        if latitude == 0 or longitude == 0:
            continue
        
        if dist > 100.0:
            drv.save_screenshot('./images/screenshot.jpg')
            if not flags:
                t1 = time()
                drv.execute_script("push_alarm()")
                flags  = True
                show_img()
        
        if time() - t1 > 60.0:
            flags = False
        
        sleep(3)
