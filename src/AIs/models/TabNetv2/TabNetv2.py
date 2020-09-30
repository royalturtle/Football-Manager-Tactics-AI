from src.utils.TestPrinter import _TPI
from src.AIs.AI_Base import AI_Base
from src.AIs.env.tactics.tactics_inner import TacticsInner
from pytorch_tabnet.tab_model import TabNetRegressor
import numpy as np
from sklearn.metrics import mean_squared_error
from random import *
import os

class TabNetv2(AI_Base):
    file_path = os.getcwd() + "\\src\\AIs\\models\\TabNetv1\\"
    save_name = file_path + "garbage_model"

    def __init__(self, *args, **kwargs):
        _TPI(self, locals())
        super(TabNetv2, self).__init__(*args, **kwargs)

        col_nums = 36
        player_nums = 22

        cat_idxs = list()
        cat_dims = list()
        cat_emb_dim = list()
        for i in range(22):
            cat_idxs += [0 + i * col_nums, 1 + i * col_nums]
            cat_dims += [2, 24]
            cat_emb_dim += [1, 8]

        self.cat_idxs = cat_idxs
        self.cat_dims = cat_dims
        self.cat_emb_dim = cat_emb_dim

        self.ai = TabNetRegressor(
            input_dim=col_nums * player_nums,
            cat_dims=self.cat_dims,
            cat_emb_dim=self.cat_emb_dim,
            cat_idxs=self.cat_idxs
        )
        '''
        save = self.save_name + ".zip"
        print(save)
        if os.path.isfile(save):
            print("Load Network")
            self.ai.load_model(save)
        '''

        ACT = self.env.act
        MATCH = self.env.match_loader

        self._scenario_tactics = list([
            [1, ACT.act_activate_window],
            [self.epochs,
                [1, ACT.act_move_to_statistics_window],
                [self.batches,
                    ACT.act_get_lineup,
                    self.act_get_players_data,
                    self.act_run_ai_with_learn,
                    ACT.act_change_tactics,
                    ACT.act_run_instant_match],
                [1, ACT.act_wait_match_finished],
                [1, ACT.act_close_match_result_window],
                [1, ACT.act_get_matches_result],
                [1, self.act_ai_learn],
                [1, ACT.act_load_save_file],
                [1, ACT.act_wait_save_is_loaded],
            ],
        ])

        self._scenario_matches = list([
            ACT.act_activate_window,
            ACT.act_move_to_statistics_window
        ])

        self._scenario_learn_from_file = list([
            [1,
                # [self.epochs,
                [1,
                    # [len(MATCH),
                    [1,
                        #(self.act_register_data, dict(data=MATCH.act_get(is_flat=True))),
                         self.act_run_ai_with_learn,
                         self.act_test
                         # self.act_ai_learn,
                         # MATCH.act_next
                    ]
                ],
            ]
        ])

        self.set_mode(self.mode)

    def act_register_data(self, data, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            self.players = data[0]
            self.tactics = data[1]
            self.plus = data[2]
            self.minus = data[3]

    def get_target(self, type):
        if type == 'train':
            list1 = self.env.match_loader.train_target
            list2 = self.env.match_loader.train_target2
        elif type == 'valid':
            list1 = self.env.match_loader.valid_target
            list2 = self.env.match_loader.valid_target2
        else:
            list1 = self.env.match_loader.test_target
            list2 = self.env1.match_loader.test_target2

        l1: np.array = np.array(list1).reshape(1, -1).T
        l2: np.array = np.array(list2).reshape(1, -1).T
        return np.concatenate((l1, l2), axis=1).reshape(-1, 1)

    def act_test(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            X_test = np.array(self.env.match_loader.test_players)
            y_test = self.get_target('test')

            preds = self.ai.predict(X_test)
            y_true = y_test
            test_score = mean_squared_error(y_pred=preds, y_true=y_true)
            print(test_score)

    def act_run_ai_with_learn(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            X_train = np.array(self.env.match_loader.train_players)
            y_train = self.get_target('train')
            X_valid = np.array(self.env.match_loader.valid_players)
            y_valid = self.get_target('valid')

            self.ai.fit(
                X_train=X_train, y_train=y_train,
                X_valid=X_valid, y_valid=y_valid,
                max_epochs=500,
                patience=500,
                batch_size=512,
                drop_last=False
            )

            self.ai.save_model(self.save_name)


