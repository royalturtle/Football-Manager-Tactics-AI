from src.utils.TestPrinter import _TPI
from src.AIs.AI_Base import AI_Base
from src.AIs.actor.Actions import Actions as ACT


class TestModel(AI_Base):
    _scenario_tactics = [
        ACT.act_activate_window,
        ACT.act_move_to_statistics_window
    ]

    def __init__(self, mode="TEST_TACTICS"):
        _TPI(self, locals())
        super().__init__()

        self.set_mode(mode)
