import torch
import torch.nn as nn


from src.utils.TestPrinter import _TPI
from src.AIs.AI_Base import AI_Base
from src.AIs.models.RNNv0.contants import *


class RNNfield(nn.Module):
    def __init__(self, in_size, classes_no, time_steps=10):
        super(RNNfield, self).__init__()

        self.model = nn.Sequential(
            nn.LSTM(in_size, classes_no),
        )

    def forward(self, x):
        return

class RNNkeeper(nn.Module):
    def __init__(self, in_size, classes_no):
        pass

class RNNmulti:
    def __init__(self):
        self.rnn_field = RNNfield()
        self.rnn_keeper = RNNkeeper()

    def run(self, x):
        pass


class RNNv0(AI_Base):
    def __init__(self, *args, **kwargs):
        _TPI(self, locals())
        super(RNNv0, self).__init__(*args, **kwargs)

        ACT = self.env.act
        DATA = self.env.data

        self._scenario_predict_data = list([
            [1, self.act_output_console]
        ])

        self.rnn_plus = RNNmulti()
        self.rnn_minus = RNNmulti()

        self.plus = 0
        self.minus = 0

    def act_output_console(self, is_test=False):
        print("[Plus : {}][Minus : {}]".format(self.plus, self.minus))

    def act_set_input(self, x):
        self.input = x

    def act_get_plus(self):
        self.plus = self.rnn_plus.run(self.input)

    def act_get_minus(self, x):
        self.minus = self.rnn_minus.run(self.input)
