from src.utils.TestPrinter import _TPI
from src.constants.constant_networks import *
from src.AIs.AI_Base import AI_Base


class Agent:
    def __init__(self, ai_name=None, mode=None, epochs=1, players=1):
        _TPI(self, locals())
        assert ai_name is not None, "You didn't select any ai model."
        assert mode is not None, "You didn't select any mode."

        def get_network_available(name):
            assert name in available_networks, "Available : {} / Inp : {}".format(str(available_networks.keys()), name)
            return available_networks[name]

        self.ai_network: AI_Base = get_network_available(ai_name)(
            mode=mode,
            epochs=epochs,
            players=players
        )

    def run(self):
        _TPI(self, locals())
        self.ai_network.run(self.ai_network.scenario)
