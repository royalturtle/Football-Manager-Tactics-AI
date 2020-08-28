from src.utils.TestPrinter import _TPI
from src.AIs.constant_networks import *
from src.AIs.AI_Base import AI_Base


class Agent:
    def __init__(self, ai_name=None, mode=None):
        _TPI(self, locals())
        assert ai_name is not None, "You didn't select any ai model."
        assert mode is not None, "You didn't select any mode."

        def get_network_available(name):
            assert name in available_networks, "Available : {} / Inp : {}".format(str(available_networks.keys()), name)
            return available_networks[name]

        self.ai_network: AI_Base = get_network_available(ai_name)(mode)

    def run(self):
        _TPI(self, locals())
        self.ai_network.run()
