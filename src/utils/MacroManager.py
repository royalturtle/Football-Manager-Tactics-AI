import pyautogui
import time
import mss
import mss.tools
import numpy as np
import pyperclip
pyautogui.FAILSAFE = True


class MacroManager:
    @staticmethod
    def move_sleep(position, sleep=0):
        pyautogui.moveTo(position)
        time.sleep(sleep)

    @staticmethod
    def move_click(position, num=1):
        pyautogui.moveTo(position)
        for i in range(num):
            pyautogui.click()

    @staticmethod
    def move_click_sleep(position, num=1, sleep=0):
        pyautogui.moveTo(position)
        for i in range(num):
            pyautogui.click()
            time.sleep(sleep)

    @staticmethod
    def press_sleep(key, sleep):
        pyautogui.press(key)
        time.sleep(sleep)

    @staticmethod
    def cmd_key(cmd, key):
        pyautogui.keyDown(cmd)
        pyautogui.press(key)
        pyautogui.keyUp(cmd)

    @staticmethod
    def mouse_ocr(point1, point2):
        pyautogui.moveTo(point1)
        MacroManager.cmd_key('winleft', 'q')
        MacroManager.move_click_sleep(point2, 1, 1)
        MacroManager.cmd_key('ctrl', 'a')
        MacroManager.cmd_key('ctrl', 'c')
        pyautogui.press('esc')
        return pyperclip.paste()

    @staticmethod
    def screen_check(top, left, value, width=1, height=1):
        boolean = True
        while boolean:
            time.sleep(3)

            with mss.mss() as sct:
                monitor_number = 2
                mon = sct.monitors[monitor_number]
                monitor = {
                    "top": mon["top"] + top,
                    "left": mon["left"] + left,
                    "width": width,
                    "height": height,
                    "mon": monitor_number,
                }
                sct_img = sct.grab(monitor)
                img = np.array(sct_img)
                print(img)

            for i in range(len(img[0][0])):
                if img[0][0][i] != value[i]:
                    boolean = False
                    break

    @staticmethod
    def check_wait_until_color_find_in_screen(top, left, value, width=1, height=1):
        boolean = True
        while boolean:
            time.sleep(3)

            with mss.mss() as sct:
                monitor_number = 2
                mon = sct.monitors[monitor_number]
                monitor = {
                    "top": mon["top"] + top,
                    "left": mon["left"] + left,
                    "width": width,
                    "height": height,
                    "mon": monitor_number,
                }
                sct_img = sct.grab(monitor)
                img = np.array(sct_img)
                print(img)

            for i in range(len(img[0][0])):
                if img[0][0][i] == value[i]:
                    boolean = False
                    break


    class Test:
        @staticmethod
        def mouse_position_h(base, height, num):
            pyautogui.moveTo(base)
            for i in range(num):
                time.sleep(1)
                pyautogui.moveTo((base[0], base[1]+height*i))

        @staticmethod
        def check_color_of_mouse(top, left, width=1, height=1):
            pyautogui.moveTo(top, left)
            with mss.mss() as sct:
                monitor_number = 2
                mon = sct.monitors[monitor_number]
                monitor = {
                    "top": mon["top"] + top,
                    "left": mon["left"] + left,
                    "width": width,
                    "height": height,
                    "mon": monitor_number,
                }
                sct_img = sct.grab(monitor)
                img = np.array(sct_img)
                print(img)
