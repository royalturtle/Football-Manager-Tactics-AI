import time
import pyperclip
import pyautogui

from src.utils.MacroManager import MacroManager as MACRO
from src.utils.TestPrinter import _TPI


CLASS_NAME = "Actions"


class Actions:
    @staticmethod
    def act_activate_window(is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            MACRO.move_click((-609, 916,))

    @staticmethod
    def act_move_to_statistics_window(is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            MACRO.press_sleep('space', 1.4)
            MACRO.press_sleep('space', 1.4)
            MACRO.press_sleep('space', 2.8)

    @staticmethod
    def act_run_instant_match(is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            MACRO.move_click_sleep((-174, 104,), 1, 1)
            MACRO.move_click_sleep((-114, 180,), 1, 1)
            MACRO.press_sleep('space', 2)

    @staticmethod
    def act_wait_match_finished(is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            MACRO.check_wait_until_color_find_in_screen(200, 1000, [46, 29, 5, 255])

    @staticmethod
    def act_close_match_result_window(players=1, is_test=False):
        for i in range(players // 2 + 1):
            if is_test is True:
                _TPI(CLASS_NAME, locals())
            else:
                MACRO.move_click((-170, 333), 1)

    @staticmethod
    def act_load_save_file(save_name=None, is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            MACRO.cmd_key('ctrl', 'o')
            time.sleep(2)
            pyperclip.copy(save_name[:len(save_name) - 1])
            MACRO.cmd_key('ctrl', 'v')
            pyautogui.typewrite(")")
            MACRO.press_sleep('enter', 0.1)

            # 로딩 끝나기 인식
            MACRO.screen_check(33 + 279, 1920 - 1652, [29, 22, 15, 255])

    @staticmethod
    def act_change_tactics(is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            raise NotImplementedError("ERROR")

    @staticmethod
    def act_load_player_data(is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            raise NotImplementedError("ERROR")

    @staticmethod
    def act_multiple_run_instant_matches(players=1, is_test=False):
        for i in range(players):
            Actions.act_run_instant_match(is_test)

    @staticmethod
    def act_get_matches_result(is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            raise NotImplementedError("ERROR")

    @staticmethod
    def act_wait_save_is_loaded(is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            raise NotImplementedError("ERROR")

    @staticmethod
    def act_get_lineup(is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            raise NotImplementedError("ERROR")

