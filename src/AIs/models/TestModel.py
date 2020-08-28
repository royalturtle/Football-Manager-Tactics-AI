from src.utils.TestPrinter import _TPI
from src.AIs.AI_Base import AI_Base
from src.AIs.actor.Actions import Actions as ACT


class TestModel(AI_Base):
    _scenario_tactics = [
        ACT.act_activate_window,
        ACT.act_move_to_statistics_window,
        ACT.act_multiple_change_tactics_and_run_instant_matches,
        ACT.act_wait_match_finished,
        ACT.act_close_match_result_window,
        ACT.act_get_matches_result,
        ACT.act_load_save_file,
        ACT.act_wait_save_is_loaded
    ]

    _scenario_matches = [
        ACT.act_activate_window,
        ACT.act_move_to_statistics_window
    ]

    def __init__(self, mode="TEST_TACTICS"):
        _TPI(self, locals())
        super().__init__()

        self.set_mode(mode)
