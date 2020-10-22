from src.AIs.models.TabNetBase.TabNetBase import TabNetBase
from src.utils.TestPrinter import _TPI
from pytorch_tabnet.tab_model import TabNetClassifier


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
                    result = 1
                elif result > 0:
                    result = 2
                self.y_train[i] = result

            for i in range(len(self.y_valid)):
                result = MATCH.valid_plus[i] - MATCH.valid_minus[i]
                if result < 0:
                    result = 1
                elif result > 0:
                    result = 2
                self.y_valid[i] = result

            for i in range(len(self.y_valid)):
                result = MATCH.test_plus[i] - MATCH.test_minus[i]
                if result < 0:
                    result = 1
                elif result > 0:
                    result = 2
                self.y_test[i] = result

