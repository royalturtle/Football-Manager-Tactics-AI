from src.utils.TestPrinter import _TPI
from src.AIs.models.TabNetBase.TabNetBase import TabNetBase


class TabNetv1(TabNetBase):
    def act_modify_data(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            self.y_train = self.y_train.reshape(-1, 1)
            self.y_valid = self.y_train.reshape(-1, 1)
            self.y_test = self.y_test.reshape(-1, 1)
