from src.utils.TestPrinter import _TPI
from src.AIs.AI_Base import AI_Base


class TestModel(AI_Base):
    def __init__(self, *args, **kwargs):
        _TPI(self, locals())
        super(TestModel, self).__init__(*args, **kwargs)

        ACT = self.env.act

        self._scenario_tactics = list([
            [1, ACT.act_activate_window],
            [self.epochs,
             [1, ACT.act_move_to_statistics_window],
             [self.players,
              ACT.act_get_lineup,
              self.act_get_players_data,
              self.act_run_ai_with_learn,
              ACT.act_change_tactics,
              ACT.act_run_instant_match],
             [1, ACT.act_wait_match_finished],
             [1, ACT.act_close_match_result_window],
             [1, ACT.act_get_matches_result],
             [1, self.act_ai_learn],
             [1, ACT.act_load_save_file],
             [1, ACT.act_wait_save_is_loaded],
            ],
        ])

        self._scenario_matches = list([
            ACT.act_activate_window,
            ACT.act_move_to_statistics_window
        ])

        self.set_mode(self.mode)
