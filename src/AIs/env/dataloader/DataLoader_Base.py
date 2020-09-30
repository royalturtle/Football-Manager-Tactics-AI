import numpy as np
import pandas as pd

from src.constants.constant_data import ConstantData
from src.utils.TestPrinter import _TPI


class DataLoader_Base:
    def __init__(self, files, players):
        _TPI(self, locals())
        self.length = ConstantData.length()

        if self.length == 1:
            assert (type(files) is str), "INVALID count of dataloader files, or wrong file path"
        assert self.length == len(files), "INVALID count of dataloader files, or wrong file path"

        self.data = list()
        print(files)
        for i in range(self.length):
            self.data.append(pd.read_csv(files[i]))
