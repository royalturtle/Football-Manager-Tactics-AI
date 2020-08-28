import time
import pyperclip
import pyautogui
from src.utils.MacroManager import MacroManager as MACRO


class Actions:
    @staticmethod
    def test_action_1(is_test=False):
        print("test1")

    @staticmethod
    def test_action_2():
        print("test2")

    @staticmethod
    def act_activate_window(is_test=False):
        if is_test is True:
            print("act_activate_window")
        else:
            MACRO.move_click((-609, 916,))

    @staticmethod
    def act_move_to_statistics_window(is_test=False):
        if is_test is True:
            print("act_move_to_statistics_window")
        else:
            MACRO.press_sleep('space', 1.4)
            MACRO.press_sleep('space', 1.4)
            MACRO.press_sleep('space', 2.8)

    @staticmethod
    def act_run_instant_match(is_test=False):
        if is_test is True:
            print("act_run_instant_match")
        else:
            MACRO.move_click_sleep((-174, 104,), 1, 1)
            MACRO.move_click_sleep((-114, 180,), 1, 1)
            MACRO.press_sleep('space', 2)

    @staticmethod
    def act_wait_match_finished(is_test=False):
        if is_test is True:
            print("act_wait_match_finished")
        else:
            MACRO.check_wait_until_color_find_in_screen(200, 1000, [46, 29, 5, 255])

    @staticmethod
    def act_close_match_result_window(is_test=False):
        if is_test is True:
            print("act_close_match_result_window")
        else:
            MACRO.move_click((-170, 333), 1)

    @staticmethod
    def act_load(save_name, is_test=False):
        if is_test is True:
            print("act_load")
        else:
            MACRO.cmd_key('ctrl', 'o')
            time.sleep(2)
            pyperclip.copy(save_name[:len(save_name) - 1])
            MACRO.cmd_key('ctrl', 'v')
            pyautogui.typewrite(")")
            MACRO.press_sleep('enter', 0.1)

            # 로딩 끝나기 인식
            MACRO.screen_check(33 + 279, 1920 - 1652, [29, 22, 15, 255])
