import copy

from src.utils.TestPrinter import _TPI
from src.AIs.AI_Base import AI_Base
from src.AIs.env.tactics.tactics_inner import TacticsInner


class DataCollector(AI_Base):
    def __init__(self, *args, **kwargs):
        _TPI(self, locals())
        super(DataCollector, self).__init__(*args, **kwargs)

        ACT = self.env.act

        self._scenario_tactics = list([
            [1, ACT.act_activate_window],
            [self.epochs,
                [1, ACT.act_move_to_statistics_window],
                [self.batches,
                    ACT.act_get_lineup,
                    ACT.act_change_tactics,
                    ACT.act_run_instant_match],
                [1, ACT.act_wait_match_finished],
                [1, ACT.act_close_match_result_window],
                [1, ACT.act_get_matches_result],
                [1, ACT.act_load_save_file],
                [1, ACT.act_wait_save_is_loaded],
            ],
        ])

        self._scenario_matches = copy.deepcopy(self._scenario_tactics)
        self.set_mode(self.mode)
