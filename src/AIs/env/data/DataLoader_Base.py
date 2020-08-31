import pandas as pd
import copy


from src.constants.constant_game import constant_data


class InputManager:
    def __init__(self, files):

        self.data = copy.deepcopy(constant_data)
        for i, file in enumerate(files):
            self.data[i]["env"] = pd.read_csv(files[i])

    def get_stats_by_ids(self):
        pass
