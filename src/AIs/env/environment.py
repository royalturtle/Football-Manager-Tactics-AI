import numpy as np

from src.utils.TestPrinter import _TPI
from src.AIs.env.actor.Actions import Actions
from src.AIs.env.dataloader.DataLoader_FM import DataLoaderFM
from src.AIs.env.MatchLoader import MatchLoader

from src.constants.constant_data import constant_data
from src.constants.constant_file import ConstantFile


class Environment:
    def __init__(self, csv_field: str = None, csv_keeper: str = None, players: int = 1):
        _TPI(self, locals())
        self.Actions = Actions
        self.data_loader = DataLoaderFM(files=(ConstantFile.file_fd(),ConstantFile.file_gk()), players=players)
        self.match_loader = MatchLoader()

    def get_players_stat(self, team):
        _TPI(self, locals())
        result = None
        return result

    @property
    def act(self):
        return self.Actions

    @property
    def data(self):
        _TPI(self, locals())
