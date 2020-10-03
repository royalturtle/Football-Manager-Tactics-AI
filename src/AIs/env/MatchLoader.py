import os
from os import listdir
from os.path import isfile, join
import json

from src.utils.TestPrinter import _TPI


class MatchLoader:
    filepath = os.getcwd() + "/matches/"

    def __init__(self):
        self.files = [f for f in listdir(self.filepath) if isfile(join(self.filepath, f))]
        self.index = 0
        self.file = self.files[self.index]
        self.test_num = int(len(self.files) * 0.1)

        def set_trainset(obj):
            _players = list()
            target = list()
            target2 = list()

            for i in range(0, len(obj)):
                players, tactics, plus, minus = obj.act_get(ind=i, is_flat=True)

                for data in players:
                    _players.append(data)

                for data in plus:
                    target.append(data)

                for data in minus:
                    target2.append(data)

            return _players, target, target2

        self.train_players, self.train_target, self.train_target2 = set_trainset(self)

        def set_validset(obj):
            _players = list()
            _target = list()
            _target2 = list()

            for i in range(len(obj), len(obj)+obj.test_num):
                players, tactics, plus, minus = obj.act_get(ind=i, is_flat=True)

                for data in players:
                    _players.append(data)

                for data in plus:
                    _target.append(data)

                for data in minus:
                    _target2.append(data)

            return _players, _target, _target2

        self.valid_players, self.valid_target, self.valid_target2 = set_validset(self)

        def set_testset(obj):
            _players = list()
            _target = list()
            _target2 = list()

            for i in range(len(obj)+obj.test_num, len(obj.files)):
                players, tactics, plus, minus = obj.act_get(ind=i, is_flat=True)

                for data in players:
                    _players.append(data)

                for data in plus:
                    _target.append(data)

                for data in minus:
                    _target2.append(data)

            return _players, _target, _target2

        self.test_players, self.test_target, self.test_target2 = set_testset(self)

    def act_next(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            self.index += 1
            # self.file = self.files[self.index]

    def act_get(self, ind=None, is_flat=False, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            if ind is None:
                filename = self.files[self.index]
            else:
                filename = self.files[ind]

            with open(self.filepath + filename, 'r') as f:
                data_list = json.load(f)
                result = list()
                tactics = list()
                plus = list()
                minus = list()

                for data in data_list:
                    one_data = list()
                    my_team = data['m']
                    for player in my_team:
                        player.insert(0, 0)
                        if is_flat:
                            one_data += player
                        else:
                            one_data.append(player)

                    your_team = data['o']
                    for player in your_team:
                        player.insert(0, 1)
                        if is_flat:
                            one_data += player
                        else:
                            one_data.append(player)

                    result.append(one_data)

                    tactics.append(data['t'])
                    plus.append(data['s'])
                    minus.append(data['l'])

                return result, tactics, plus, minus

    def __len__(self):
        # return len(self.files)
        return len(self.files) - 2 * self.test_num
