import pyautogui
import time


def relic():
    retry_image = 'assets/retry.png'
    ok = 'assets/OK.png'
    full = 'assets/Relic/retry.png'
    low = 'assets/Relic/Low.png'
    confirm = 'assets/Confirm.png'

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
    
    retry()


def shadow():
    retry_image = 'assets/Shadow/retry.png'
    ok = 'assets/OK.png'
    full = 'assets/full.png'
    low = 'assets/Shadow/Low.png'
    confirm = 'assets/Confirm.png'

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

    retry()



shadow()