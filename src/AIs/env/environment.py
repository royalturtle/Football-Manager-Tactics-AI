from src.utils.TestPrinter import _TPI
from src.AIs.env.actor.Actions import Actions


class Environment:
    def __init__(self, csv_player: str = None, csv_field: str = None, csv_keeper: str = None):
        _TPI(self, locals())
        self.Actions = Actions

        def load_data_file():
            pass

    def get_players_stat(self, team):
        _TPI(self, locals())
        result = None
        return result

    @property
    def act(self):
        return self.Actions

