from src.utils.TestPrinter import _TPI
from src.AIs.AI_Base import AI_Base
from src.AIs.env.tactics.tactics_inner import TacticsInner


class TestModel(AI_Base):
    def __init__(self, *args, **kwargs):
        _TPI(self, locals())
        super(TestModel, self).__init__(*args, **kwargs)

        ACT = self.env.act
        MATCH = self.env.match_loader

        self._scenario_tactics = list([
            [1, ACT.act_activate_window],
            [self.epochs,
                [1, ACT.act_move_to_statistics_window],
                [self.batches,
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

        self._scenario_learn_from_file = list([
            # [self.epochs,
            [4,
                [len(MATCH),
                     # MATCH.act_get,
                     self.act_get_players_data,
                     self.act_run_ai_with_learn,
                     self.act_ai_learn,
                     MATCH.act_next
                ]
            ]
        ])

        self.set_mode(self.mode)

    @staticmethod
    def test_get_result():
        return [
            {
                "GF": 3,
                "GA": 1,
                "lineup": TacticsInner.get_lineup(is_test=True),
                "formation": TacticsInner.get_formation_by_index(0),
                "tactics": TacticsInner.get_tactics_by_index(0)
            },
            {
                "GF": 1,
                "GA": 1,
                "lineup": TacticsInner.get_lineup(is_test=True),
                "formation": TacticsInner.get_formation_by_index(1),
                "tactics": TacticsInner.get_tactics_by_index(1)
            },
            {
                "GF": 0,
                "GA": 0,
                "lineup": TacticsInner.get_lineup(is_test=True),
                "formation": TacticsInner.get_formation_by_index(2),
                "tactics": TacticsInner.get_tactics_by_index(2)
            },
            {
                "GF": 0,
                "GA": 3,
                "lineup": TacticsInner.get_lineup(is_test=True),
                "formation": TacticsInner.get_formation_by_index(3),
                "tactics": TacticsInner.get_tactics_by_index(3)
            },
            {
                "GF": 1,
                "GA": 2,
                "lineup": TacticsInner.get_lineup(is_test=True),
                "formation": TacticsInner.get_formation_by_index(4),
                "tactics": TacticsInner.get_tactics_by_index(4)
            },
            {
                "GF": 2,
                "GA": 1,
                "lineup": TacticsInner.get_lineup(is_test=True),
                "formation": TacticsInner.get_formation_by_index(5),
                "tactics": TacticsInner.get_tactics_by_index(5)
            }
        ]
