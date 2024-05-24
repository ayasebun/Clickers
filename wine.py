import time
import pyautogui
import sys

try:
    while True:

        print("Buying Peyton Wine")
        time.sleep(0.5)

        # Select Wine
        pyautogui.click(button='right',clicks=3,interval=0.25,x=840,y=530)
        time.sleep(1)

        # Hit the buy button
        pyautogui.click(button='left',clicks=3,interval=0.25,x=930,y=920)

        """
        buff = n

        where n is the number of seconds to wait.
        The CD in game is 60 seconds but adding additional wait to it in case
        There's some weird shit with the way that SG handles CDs
        """

        buff = 61
        print("61s buffer. Please CTRL-C here if you need to escape.\n")
        for i in range(0, buff):
            print(".", end = " ")
            time.sleep(1)
        print("\n")

except KeyboardInterupt:
    print('\nExiting.\n')