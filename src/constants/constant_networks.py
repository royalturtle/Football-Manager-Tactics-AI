from src.AIs.models.FFNNv0.FFNNv0 import FFNNv0
from src.AIs.models.TestModel.TestModel import TestModel
from src.AIs.models.RNNv0.RNNv0 import RNNv0
from src.AIs.models.TabNetv1.TabNetv1 import TabNetv1
from src.AIs.models.TabNetCv0.TabNetCv0 import TabNetCv0
from src.AIs.models.TabNetCv1.TabNetCv1 import TabNetCv1
from src.AIs.models.DataCollector.DataCollector import DataCollector

# Constants
available_networks = {
    "TestModel": TestModel,
    "FFNNv0": FFNNv0,
    "RNNv0": RNNv0,
    "DataCollector": DataCollector,
    "TabNetv1": TabNetv1,
    "TabNetCv0": TabNetCv0,
    "TabNetCv1": TabNetCv1
}
