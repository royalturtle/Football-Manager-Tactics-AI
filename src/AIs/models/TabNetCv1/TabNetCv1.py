from src.AIs.models.TabNetBase.TabNetBase import TabNetBase
from src.utils.TestPrinter import _TPI
from pytorch_tabnet.tab_model import TabNetClassifier
import numpy as np


class TabNetCv1(TabNetBase):
    def act_init_ai(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            MATCH = self.env.match_loader
            self.ai = TabNetClassifier(
                n_steps=10,
                input_dim=MATCH.count_cols * MATCH.count_players,
                cat_dims=self.cat_dims,
                cat_emb_dim=self.cat_emb_dim,
                cat_idxs=self.cat_idxs,
                device_name='cuda'
            )

    def act_modify_data(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            MATCH = self.env.match_loader
            for i in range(len(self.y_train)):
                result = MATCH.train_plus[i] - MATCH.train_minus[i]

                if result < 0:
                    result = 0
                elif result == 0:
                    result = 1
                else:
                    result = 2
                self.y_train[i] = result

            for i in range(len(self.y_valid)):
                result = MATCH.valid_plus[i] - MATCH.valid_minus[i]
                if result < 0:
                    result = 0
                elif result == 0:
                    result = 1
                else:
                    result = 2
                self.y_valid[i] = result

            for i in range(len(self.y_valid)):
                result = MATCH.test_plus[i] - MATCH.test_minus[i]
                if result < 0:
                    result = 0
                elif result == 0:
                    result = 1
                else:
                    result = 2
                self.y_test[i] = result

    def load_model(self):
        print("Loading Model")
        print(self.save_name + ".zip")
        self.ai.load_model(self.save_name + ".zip")

    def get_result(self, my_team:list, your_team:list):
        # tmp
        '''
        MATCH = self.env.match_loader
        self.act_register_data(data=MATCH.act_get(is_flat=True))
        self.act_modify_data()
        self.ai = TabNetClassifier(
            n_steps=10,
            input_dim=MATCH.count_cols * MATCH.count_players,
            cat_dims=self.cat_dims,
            cat_emb_dim=self.cat_emb_dim,
            cat_idxs=self.cat_idxs,
            device_name='cuda'
        )

        self.ai.fit(
            X_train=self.X_train, y_train=self.y_train,
            X_valid=self.X_valid, y_valid=self.y_valid,
            max_epochs=self.epochs,
            patience=500,
            batch_size=512,
            drop_last=False
        )
        '''
        try:
            x = list()
            for player in my_team:
                x.append(0)
                x.extend(player)

            for player in your_team:
                x.append(1)
                x.extend(player)

            x = np.array(x)
            x = np.array([x])
            print(x.shape)

            # predictions = self.ai.predict(x)
            probability = self.ai.predict_proba(x)
            print(probability)

            return probability[0][2]

        except Exception as e:
            print(e)
