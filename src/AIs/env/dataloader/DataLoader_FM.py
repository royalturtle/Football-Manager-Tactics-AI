from src.AIs.env.dataloader.DataLoader_Base import DataLoader_Base
from src.constants.constant_game import ConstantGame


class DataLoaderFM(DataLoader_Base):
    FILE_NAN = -1
    FILE_FD = 0
    FILE_GK = 1

    COL_ID = 0
    COL_NAME = 1
    COL_STAT = 2

    def __init__(self, *args, **kwargs):
        super(DataLoaderFM, self).__init__(*args, **kwargs)

    def get_stats_by_nickname(self, names, position=None, is_only_stats=False):
        players_gk = names[0]
        players_fd = names[1:]

        _data = self.data[self.FILE_GK]
        result_gk = _data[_data.nickname == players_gk]

        _data = self.data[self.FILE_FD]
        result_fd = _data[_data.nickname.isin(players_fd)]

        if is_only_stats is True:
            result_gk = result_gk.iloc[:, self.COL_STAT:]
            result_fd = result_fd.iloc[:, self.COL_STAT:]

        if position is not None:
            assert len(names) == len(position), "length of names is different with length of position info"
            col_name = "position"
            result_gk.insert(0, col_name, 0)

            col_position = list()
            for i in range(1, len(position)):
                col_position.append(ConstantGame.position_index(position[i]))

            result_fd.insert(0, col_name, col_position)

        return result_fd, result_gk



