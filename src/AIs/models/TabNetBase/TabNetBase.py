from src.utils.TestPrinter import _TPI
from src.AIs.AI_Base import AI_Base
from src.AIs.env.tactics.tactics_inner import TacticsInner
from pytorch_tabnet.tab_model import TabNetRegressor
import numpy as np
from sklearn.metrics import mean_squared_error
import os


class TabNetBase(AI_Base):
    file_path = os.getcwd() + "\\src\\AIs\\models\\TabNetv1\\"
    save_name = file_path + "garbage_model"

    def __init__(self, *args, **kwargs):
        _TPI(self, locals())
        super(TabNetBase, self).__init__(*args, **kwargs)
        ACT = self.env.act
        MATCH = self.env.match_loader

        self.X_train, self.X_valid, self.X_test = None, None, None
        self.y_train, self.y_valid, self.y_test = None, None, None
        self.cat_idxs, self.cat_dims, self.cat_emb_dim = MATCH.get_categorical()
        self.ai = None

        self._scenario_tactics = None
        self._scenario_matches = None

        self._scenario_learn_from_file = list([
            [1,
                # [self.epochs,
                [1,
                    # [len(MATCH),
                    [1,
                        (self.act_register_data, dict(data=MATCH.act_get(is_flat=True))),
                         self.act_modify_data,
                         self.act_init_ai,
                         # self.act_load_game,
                         self.act_run_ai_with_learn,
                         self.act_test
                    ]
                ],
            ]
        ])

        self.set_mode(self.mode)

    def act_register_data(self, data, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            self.X_train = np.array(self.env.match_loader.train_players)
            self.y_train = np.array(self.env.match_loader.train_target)
            self.X_valid = np.array(self.env.match_loader.valid_players)
            self.y_valid = np.array(self.env.match_loader.valid_target)
            self.X_test = np.array(self.env.match_loader.test_players)
            self.y_test = np.array(self.env.match_loader.test_target)

    def act_init_ai(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            MATCH = self.env.match_loader
            self.ai = TabNetRegressor(
                n_steps=10,
                input_dim=MATCH.count_cols * MATCH.count_players,
                cat_dims=self.cat_dims,
                cat_emb_dim=self.cat_emb_dim,
                cat_idxs=self.cat_idxs
            )

    def act_modify_data(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            pass

    def act_load_game(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            save = self.save_name + ".zip"
            if os.path.isfile(save):
                print("Load Network")
                self.ai.load_model(save)

    def act_test(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            predictions = self.ai.predict(self.X_test)
            y_true = self.y_test
            test_score = mean_squared_error(y_pred=predictions, y_true=y_true)
            np.savetxt("predict.txt", predictions, delimiter=',', fmt='%d')
            np.savetxt("true.txt", y_true, delimiter=',', fmt='%d')
            print(test_score)
            print(predictions[0])
            print(y_true[0])

    def act_run_ai_with_learn(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            self.ai.fit(
                X_train=self.X_train, y_train=self.y_train,
                X_valid=self.X_valid, y_valid=self.y_valid,
                max_epochs=self.epochs,
                patience=500,
                batch_size=512,
                drop_last=False
            )

            self.ai.save_model(self.save_name)


