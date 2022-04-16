from PIL import ImageGrab
from cv2 import threshold
import pyautogui as ag
import cv2 as cv
import numpy as np
import keyboard as k
import time
import os
import threading


def closeKey():
    while 1:
        if k.is_pressed("r"):
            os._exit(0)


threading.Thread(target=closeKey, args=()).start()


def rightClick():
    ag.rightClick()


def type(string):
    for x in string:
        k.press(x)


ccp = [1020, 469]
tHold = 0.8
caughtFish = 0
totalFish = 0
fishingImg = cv.imread("fishing.png", cv.IMREAD_UNCHANGED)
notFishingImg = cv.imread("not fishing.png", cv.IMREAD_UNCHANGED)

while (1):
    screen = ImageGrab.grab().load()
    if (caughtFish == 100):
        type("t/bp")
        k.press(["enter"])
        time.sleep(0.5)
        ag.click()
        time.sleep(0.5)
        k.press(["escape"])
        caughtFish = 0
    if screen[ccp[0], ccp[1]] == (252,252,84):
        caughtFish += 1
        totalFish += 1
        print("Fish caught: " + str(totalFish) )
        rightClick()
        rightClick()
        time.sleep(2)
    haystack = cv.cvtColor(np.array(ImageGrab.grab(
        bbox=(688, 975, 1231, 1038))), cv.COLOR_RGB2BGR)
    result = cv.matchTemplate(notFishingImg, haystack, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if (max_val >= tHold):
        rightClick()
