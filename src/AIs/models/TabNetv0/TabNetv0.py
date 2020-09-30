from src.utils.TestPrinter import _TPI
from src.AIs.AI_Base import AI_Base
from src.AIs.env.tactics.tactics_inner import TacticsInner
from pytorch_tabnet.tab_model import TabNetRegressor
import numpy as np
from sklearn.metrics import mean_squared_error
from random import *


class TabNetv0(AI_Base):
    def __init__(self, *args, **kwargs):
        _TPI(self, locals())
        super(TabNetv0, self).__init__(*args, **kwargs)

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
            input_dim=col_nums*player_nums,
            cat_dims=self.cat_dims,
            cat_emb_dim=self.cat_emb_dim,
            cat_idxs=self.cat_idxs
        )

        print(type(self.ai.cat_idxs))

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
                [self.epochs,
                    [len(MATCH),
                        (self.act_register_data, dict(data=MATCH.act_get(is_flat=True))),
                         self.act_run_ai_with_learn,
                         # self.act_ai_learn,
                         MATCH.act_next
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

    def act_test(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            preds = self.ai.predict(self.env.match_loader.test_players)
            y_true = self.test_target
            test_score = mean_squared_error(y_pred=preds, y_true=y_true)

    def act_run_ai_with_learn(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            X_train = list()
            y_train = list()
            X_valid = list()
            y_valid = list()

            valid_num = 2
            valids = sample(list(np.arange(self.batches)), valid_num)
            for i in range(self.batches):
                if i in valids:
                    X_valid.append(self.players[i])
                    y_valid.append(self.plus[i])
                else:
                    X_train.append(self.players[i])
                    y_train.append(self.plus[i])

            X_train = np.array(X_train)
            X_valid = np.array(X_valid)
            y_train = np.array(y_train).reshape(-1, 1)
            y_valid = np.array(y_valid).reshape(-1, 1)
            self.ai.fit(
                X_train=X_train, y_train=y_train,
                X_valid=X_valid, y_valid=y_valid,
                max_epochs=3,
                batch_size=self.batches - valid_num,
                drop_last=False
            )


