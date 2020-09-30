import copy

from src.AIs.env.tactics.Tactics_base import TacticsBase
from src.constants.constant_tactics import ConstantTactics


class TacticsInner(TacticsBase):
    def __init__(self):
        super(TacticsBase, self).__init__()

    @staticmethod
    def get_lineup(index: int = None, is_test: bool = False):
        if is_test is True:
            return [63002306, 19192323, 45030287, 66000674, 72038776, 29000029, 28059634, 98007212, 28029911, 28067790, 43094517]
        else:
            assert int is not None, "Empty index"

    @staticmethod
    def get_formation_by_index(index: int = None) -> list:
        assert index is not None, "Empty index"
        result = list()

        if index is 0:
            result = ["GK", "DR", "DCR", "DCL", "DL", "MCR", "MCL", "AMR", "AMC", "AML", "STC"]
        elif index is 1:
            result = ["GK", "DR", "DCR", "DCL", "DL", "DM", "MCR", "MCL", "AMR", "AML", "STC"]
        elif index is 2:
            result = ["GK", "DCR", "DC", "DCL", "WBR", "WBL", "MCR", "MCL", "AMCR", "AMCL", "STC"]
        elif index is 3:
            result = ["GK", "DR", "DCR", "DCL", "DL", "DM", "MCR", "MCL", "AMR", "AML", "STC"]
        elif index is 4:
            result = ["GK", "DR", "DCR", "DCL", "DL", "MCR", "MCL", "AMR", "AMC", "AML", "STC"]
        elif index is 5:
            result = ["GK", "DR", "DCR", "DCL", "DL", "DM", "MCR", "MCL", "AMC", "STCR", "STCL"]

        return result

    @staticmethod
    def get_tactics_by_index(index: int = None) -> dict:
        assert index is not None, "Empty index"
        result = copy.deepcopy(ConstantTactics)

        if (0 <= index) and (index <= 2):
            tendency = 5
            onball = [3, False, True, 1, 1, 1, 2, 2, 1, 1, 2, False, 1, 1]
            change = [2, 1, 1, 22]
            offball= [False, 4, 4, 2, False, 4, True, 1]
        elif (3 <= index) and (index <= 5):
            tendency = 5
            onball = [2, True, True, 1, 1, 1, 3, 5, 1, 1, 1, False, 1, 1]
            change = [2, 2, 1, 22]
            offball = [True, 5, 5, 3, True, 5, True, 1]
        else:
            raise Exception("Wrong Value Range")

        result["type"] = tendency

        def change_dict(dictionary, change):
            for i, k in enumerate(dictionary.keys()):
                try:
                    dictionary[k] = change[i]
                except ValueError:
                    pass

        change_dict(result["onball"], onball)
        change_dict(result["change"], change)
        change_dict(result["offball"], offball)

        return result

