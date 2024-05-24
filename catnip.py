import time
import sys
import pyautogui

print('Starting Script\n')
time.sleep(3)

try:
    while True:
        # Only loop catnip production a few times before stopping
        n = 8
        for i in range(0, n):
            # Gather Catnip Button
            pyautogui.click(clicks=1000,x=600,y=250)
            time.sleep(0.5)
            print(f"Catnip Loop x: ", i, "\n")
            
            if i == 4:
                # Refine Catnip Button x100.
                # x=1065 bc x100 button is a bit far out.
                pyautogui.click(clicks=2,x=1065,y=250)
                print("Dumping some Catnip into Wood.\n")
                time.sleep(0.5)

        # Try Catnip Field +1
        pyautogui.click(x=600,y=300)
        print("Dump into Catnip Field Upgrade.\n")
        time.sleep(0.5)
        
        # Try Pasture Upgrade +1
        pyautogui.click(x=900,y=300)
        print("Dump into Pasture Upgrade.\n")
        time.sleep(0.5)

        # Aqueducts since they don't punish you and clear out bonus minerals
        pyautogui.click(x=600,y=360)
        print("Dump Minerals into Aqueduct.\n")
        time.sleep(0.5)

        # In case we somehow have too much wood -- Barn
        pyautogui.click(x=900,y=470)
        print("Dump into Barn Upgrade.\n")
        time.sleep(0.5)
        
        # Occasionally tap in this direction to proc astronomical event
        pyautogui.click(x=1280,y=225)
        print("Tap Astro Event, just in case.\n")
        time.sleep(0.5)
        
        # Tap the Send Hunters Button
        pyautogui.click(x=90,y=515)
        print("Tapping Send Hunters to dump.\n")
        time.sleep(0.5)

        # Dump a few clicks back into Gather Catnip for buffer
        pyautogui.click(clicks=1000,x=600,y=250)
        buff = 7
        print("7s buffer. Please CTRL-C here if you need to escape.\n")
        for i in range(0, buff):
            print(".", end = " ")
            time.sleep(1)
        print("\n")
        
# Exit
except KeyboardInterupt:
    print('\nExiting\n')