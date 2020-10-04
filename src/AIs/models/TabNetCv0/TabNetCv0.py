from src.AIs.models.TabNetBase.TabNetBase import TabNetBase
from src.utils.TestPrinter import _TPI
from pytorch_tabnet.tab_model import TabNetClassifier


class TabNetCv0(TabNetBase):
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
                cat_idxs=self.cat_idxs
            )

    def act_modify_data(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            self.y_train[self.y_train > 4] = 4
            self.y_valid[self.y_valid > 4] = 4
            self.y_test[self.y_test > 4] = 4

