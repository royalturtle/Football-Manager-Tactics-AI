import time
import pyperclip
import pyautogui

from src.utils.MacroManager import MacroManager as MACRO
from src.utils.TestPrinter import _TPI
from src.constants.constant_macro import iMouse


CLASS_NAME = "Actions"


class Actions:
    @staticmethod
    def act_change_tactics_inner(tactics_index, is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            raise NotImplementedError("Error")

    @staticmethod
    def act_change_formation(formation, is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            raise NotImplementedError("Error")

    @staticmethod
    def act_change_tactics(tactics=None, is_test=False):
        if is_test is True:
            _TPI(CLASS_NAME, locals())
        else:
            stype = tactics['type']

            def get_info(type1, type2):
                return tactics[type1][type2], iMouse[type1][type2]

            def act_boolean(type1, type2):
                tmps, tmpm = get_info(type1, type2)
                if tmps:
                    MACRO.move_click_sleep((tmpm[0], tmpm[1]), 1, 0.4)

            def act_boolean_n1(type1, type2):
                tmps, tmpm = get_info(type1, type2)
                if tmps != 1:
                    MACRO.move_click_sleep((tmpm[tmps][0], tmpm[tmps][1]), 1, 0.4)

            def act_1to5_LR(type1, type2):
                tmps, tmpm = get_info(type1, type2)
                if tmps > 3:
                    moveto = (tmpm["right"][0], tmpm["right"][1])
                    MACRO.move_click_sleep(moveto, tmps - 3, 0.4)
                elif tmps < 3:
                    moveto = (tmpm["left"][0], tmpm["left"][1])
                    MACRO.move_click_sleep(moveto, 3 - tmps, 0.4)

            def act_sel3(type1, type2):
                tmps, tmpm = get_info(type1, type2)
                if tmps == 2:
                    MACRO.move_click_sleep((tmpm["opt1"][0], tmpm["opt1"][1]), 1, 0.4)
                elif tmps == 3:
                    MACRO.move_click_sleep((tmpm["opt2"][0], tmpm["opt2"][1]), 1, 0.4)

            def act_1to5_UD(type1, type2):
                tmps, tmpm = get_info(type1, type2)
                if tmps > 3:
                    moveto = (tmpm["up"][0], tmpm["up"][1] - (stype - 1) * tmpm["heightunit"],)
                    MACRO.move_click_sleep(moveto, tmps - 3, 0.4)
                elif tmps < 3:
                    moveto = (tmpm["down"][0], tmpm["down"][1] - (stype - 1) * tmpm["heightunit"],)
                    MACRO.move_click_sleep(moveto, 3 - tmps, 0.4)

            def act_multi(type1, type2):
                tmps, tmpm = get_info(type1, type2)
                if tmpm != None:
                    for i in range(len(tmpm[tmps])):
                        MACRO.move_click_sleep((tmpm[tmps][i][0], tmpm[tmps][i][1]), 1, 0.4)

            def act_1to3_LR(type1, type2):
                tmps, tmpm = get_info(type1, type2)
                if tmps > 2:
                    moveto = (tmpm["right"][0], tmpm["right"][1])
                    MACRO.move_click_sleep(moveto, 1, 0.4)
                elif tmps < 2:
                    moveto = (tmpm["left"][0], tmpm["left"][1])
                    MACRO.move_click_sleep(moveto, 1, 0.4)

            time.sleep(2)
            mouse_point = iMouse["category"]["type"]
            MACRO.move_click_sleep(mouse_point, 1, 0.2)
            MACRO.move_click((mouse_point[0], mouse_point[1] + 30 * stype))

            MACRO.move_click_sleep(iMouse["category"]["offball"], 1, 0.5)  # [1] offball
            if tactics["offball"]["offsidetrap"]:  # - offside trap
                MACRO.move_click_sleep(iMouse["offball"]["offsidetrap"], 1, 0.4)

            act_1to5_UD("offball", "offenseline")  # - offenseline
            act_1to5_UD("offball", "defenseline")  # - defense line
            act_1to3_LR("offball", "defensewidth")  # - defense width
            act_boolean("offball", "mark")  # - mark
            act_1to5_LR("offball", "pressure")  # - pressure
            act_boolean("offball", "longpassinduce")  # - longpassinduce
            act_sel3("offball", "tackle")  # - tackle

            MACRO.move_click_sleep(iMouse["category"]["change"], 1, 0.5)  # [2] change
            act_sel3("change", "ballno")  # ballno
            act_sel3("change", "ballyes")  # - ballyes
            act_sel3("change", "keepercatch")  # - keepercatch
            act_multi("change", "keepergive")  # - keepergive

            MACRO.move_click_sleep(iMouse["category"]["onball"], 1, 0.5)  # [3] onball
            act_1to5_LR("onball", "offensewidth")  # - offensewidth
            act_boolean("onball", "tospace")  # - tospace
            act_boolean("onball", "todefense")  # - todefense
            act_multi("onball", "towhere")  # - towhere
            act_boolean_n1("onball", "leftgo")  # - leftgo
            act_boolean_n1("onball", "rightgo")  # - rightgo
            act_1to5_LR("onball", "passway")  # - passway
            act_1to5_LR("onball", "tempo")  # - tempo

            tmps, tmpm = get_info("onball", "timewaste")  # - timewaste
            if tmps > 1:
                moveto = (tmpm[0], tmpm[1])
                MACRO.move_click_sleep(moveto, tmps - 1, 0.4)

            tmps, tmpm = get_info("onball", "crosstype")  # - crosstype
            MACRO.move_click_sleep((tmpm[0][0], tmpm[0][1]), 1, 0.5)
            MACRO.move_click_sleep((tmpm[tmps][0], tmpm[tmps][1]), 1, 0.5)

            tmps, tmpm = get_info("onball", "crosshow")  # - crosshow
            if tmpm != None:
                for i in range(len(tmpm[tmps])):
                    MACRO.move_click_sleep((tmpm[tmps][i][0], tmpm[tmps][i][1]), 1, 0.4)

            act_boolean("onball", "setplay")  # - setplay
            act_boolean_n1("onball", "dribble")  # - dribble
            act_boolean_n1("onball", "creativity")  # - creativity

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
            # result: str = MACRO.mouse_ocr((973, 209), (1015, 627))
            lineup = MACRO.mouse_ocr((1371, 200), (1452, 624))
            # return result.replace('F', 'R')
            return lineup
