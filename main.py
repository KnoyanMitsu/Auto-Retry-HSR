import pyautogui
import time
import sys
from platform import system

if system() == 'Windows':
    from msvcrt import getch
else:
    from getch import getch


def relic():
    retry_image = 'assets/Relic/retry.png'
    ok = 'assets/OK.png'
    full = 'assets/full.png'
    low = 'assets/Relic/Low.png'
    confirm = 'assets/Confirm.png'


    print("Relic")
    print("Press Enter if you ready")
    print("if you wrong select press Anything")

    def confirmation():
            key_stroke = getch().encode()
            if key_stroke==chr(10).encode():
                print('Starting...')
                retry()
            else:
                print('Back to Menu...')
                selection()



    def recharge():
            while True:
                try:
                    print('Need Recharge')
                    time.sleep(3)
                    ok_location = pyautogui.locateOnScreen(ok)
                    pyautogui.click(ok_location)
                    time.sleep(2)
                    full_location = pyautogui.locateOnScreen(full)
                    pyautogui.click(full_location)
                    time.sleep(2)
                    confirm_location = pyautogui.locateOnScreen(confirm)
                    pyautogui.click(confirm_location)
                    time.sleep(2)
                    pyautogui.click(confirm_location[0]+30, confirm_location[1])
                    time.sleep(2)
                    retry()
                except pyautogui.ImageNotFoundException:
                    print('Not Need Recharge')
                    retry()


    def retry():
        while True:
            try:
                retry_location = pyautogui.locateOnScreen(retry_image)


                if retry_location is not None:
                    pyautogui.click(retry_location)
                    print('Retry')

                    print('Waiting Recharge')
                    time.sleep(5)
                else:
                    time.sleep(20)
            except pyautogui.ImageNotFoundException:
                try:
                    low_location = pyautogui.locateOnScreen(low)
                    pyautogui.click(low_location)
                    recharge()
                except pyautogui.ImageNotFoundException:
                    print('Waiting')
                    time.sleep(20)
                    continue



    confirmation()


def shadow():
    retry_image = 'assets/Shadow/retry.png'
    ok = 'assets/OK.png'
    full = 'assets/full.png'
    low = 'assets/Shadow/Low.png'
    confirm = 'assets/Confirm.png'


    print("Stagnant Shadow")
    print("Press Enter if you ready")
    print("if you wrong select press Anything")

    def confirmation():
            key_stroke = getch().encode()
            if key_stroke==chr(10).encode():
                print('Starting...')
                retry()
            else:
                print('Back to Menu...')
                selection()


    while True:
        def recharge():
                while True:
                    try:
                        print('Need Recharge')
                        time.sleep(3)
                        ok_location = pyautogui.locateOnScreen(ok)
                        pyautogui.click(ok_location)
                        time.sleep(2)
                        full_location = pyautogui.locateOnScreen(full)
                        pyautogui.click(full_location)
                        time.sleep(2)
                        confirm_location = pyautogui.locateOnScreen(confirm)
                        pyautogui.click(confirm_location)
                        time.sleep(2)
                        pyautogui.click(confirm_location[0]+30, confirm_location[1])
                        time.sleep(2)
                        retry()
                    except pyautogui.ImageNotFoundException:
                        print('Not Need Recharge')
                        retry()



        def retry():
            while True:
                try:
                    retry_location = pyautogui.locateOnScreen(retry_image)


                    if retry_location is not None:
                        pyautogui.click(retry_location)
                        print('Retry')

                        print('Waiting Recharge')
                        time.sleep(5)
                    else:
                        time.sleep(20)
                except pyautogui.ImageNotFoundException:
                    try:
                        low_location = pyautogui.locateOnScreen(low)
                        pyautogui.click(low_location)
                        recharge()
                    except pyautogui.ImageNotFoundException:
                        print('Waiting')
                        time.sleep(20)
                        continue
        
    confirmation()

def selection():
    print('Select want to auto retry:')
    print('1. Stagnant Shadow')
    print('2. Relic')
    selection=int(input("Enter your choice: "))
    if selection==1:
        shadow()
    elif selection==2:
        relic()
    else:
        print('Invalid Choice')

selection()