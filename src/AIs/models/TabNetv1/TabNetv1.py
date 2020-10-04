from src.utils.TestPrinter import _TPI
from src.AIs.models.TabNetBase.TabNetBase import TabNetBase


class TabNetv1(TabNetBase):
    def act_modify_data(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            pass
