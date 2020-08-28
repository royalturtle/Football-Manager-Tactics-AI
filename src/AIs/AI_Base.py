import copy
from src.utils.TestPrinter import _TPI
from src.AIs.constant_modes import *


class AI_Base:
    _scenario_tactics = list()
    _scenario_matches = list()

    def __init__(self, mode=None, epochs=1, players=1):
        _TPI(self, locals())
        assert mode is not None, "Running mode is not specified"

        self.scenario = list()
        self.mode = mode
        self.epochs = epochs
        self.players = players

    def run(self):
        _TPI(self, locals())
        assert self.scenario is not None, "Empty Scenario"
        for epoch in range(self.epochs):
            for action in self.scenario:
                if type(action).__name__ == "function":
                    func = action
                    func()
                else:
                    func = action[0]
                    args = action[1]
                    func(**args)

    def set_mode(self, mode):
        _TPI(self, locals())
        assert mode in available_modes, "NOT valid mode"

        def set_scenario(_self, actions: list = None):
            _self.scenario = copy.deepcopy(actions)

        def set_action_as_test(scenario) -> list:
            return_value = list()
            for item in scenario:
                if type(item).__name__ == "function":
                    return_value.append((item, dict(is_test=True)))
                else:
                    item[1]['is_test'] = True
                    return_value.append((item[0], item[1]))
            return return_value

        if mode == "TACTICS":
            assert len(self._scenario_tactics) > 0, "Scenario of tactics is empty."
            set_scenario(self, self._scenario_tactics)
        elif mode == "MATCHES":
            assert len(self._scenario_matches) > 0, "Scenario of matches is empty."
            set_scenario(self, self._scenario_matches)
        elif mode == "TEST_TACTICS":
            assert len(self._scenario_tactics) > 0, "Scenario of tactics is empty."
            test_actions: list = set_action_as_test(self._scenario_tactics)
            set_scenario(self, test_actions)
        elif mode == "TEST_MATCHES":
            assert len(self._scenario_matches) > 0, "Scenario of matches is empty."
            test_actions: list = set_action_as_test(self._scenario_matches)
            set_scenario(self, test_actions)
