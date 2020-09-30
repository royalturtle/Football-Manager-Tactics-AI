opponent = [2, 11, 0, 4, 3, 9, 12, 8, 7, 5, 14, 1, 6, 15, 10, 13]
teamA = [True, False, False, False, True, False, True, True,
         False, True, True, True, False, True, False, False]
teamB = [not i for i in teamA]
positions_id = {
            "GK": 0, "DR": 1, "DCR": 2, "DC": 3, "DCL": 4, "DL": 5,
            "WBR": 6, "DMCR": 7, "DM": 8, "DMCL": 9, "WBL": 10,
            "MR": 11, "MCR": 12, "MC": 13, "MCL": 14, "ML": 15,
            "AMR": 16, "AMCR": 17, "AMC": 18, "AMCL": 19, "AML": 20,
            "STCR": 21, "STC": 22, "STCL": 23
}


class ConstantGame:
    @staticmethod
    def count_teams():
        return len(opponent)

    @staticmethod
    def opponent(index: int= None) -> int:
        assert type(index) is int, "index should be int type"
        return opponent[index]

    @staticmethod
    def if_teamA(index: int= None) -> bool:
        assert type(index) is int, "index should be int type"
        return teamA[index]

    @staticmethod
    def if_teamB(index: int = None) -> bool:
        assert type(index) is int, "index should be int type"
        return teamB[index]

    @staticmethod
    def position_index(position: str = None):
        assert position is not None, "Parameters is empty"
        assert position in positions_id, "Wrong position string"
        return positions_id[position]
