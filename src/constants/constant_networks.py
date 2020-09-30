from src.AIs.models.FFNNv0.FFNNv0 import FFNNv0
from src.AIs.models.TestModel.TestModel import TestModel
from src.AIs.models.RNNv0.RNNv0 import RNNv0
from src.AIs.models.TabNetv0.TabNetv0 import TabNetv0
from src.AIs.models.TabNetv1.TabNetv1 import TabNetv1
from src.AIs.models.TabNetv2.TabNetv2 import TabNetv2
from src.AIs.models.TabNetv3.TabNetv3 import TabNetv3

from src.AIs.models.DataCollector.DataCollector import DataCollector

# Constants
available_networks = {
    "TestModel": TestModel,
    "FFNNv0": FFNNv0,
    "RNNv0": RNNv0,
    "DataCollector": DataCollector,
    "TabNetv0": TabNetv0,
    "TabNetv1": TabNetv1,
    "TabNetv2": TabNetv2,
    "TabNetv3": TabNetv3
}


