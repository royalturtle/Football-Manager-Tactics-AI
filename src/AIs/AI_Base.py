import copy
from src.utils.TestPrinter import _TPI
from src.AIs.constant_modes import *
from src.AIs.actor.environment import Environment


class AI_Base:
    _scenario_tactics = list()
    _scenario_matches = list()
    _scenario_learn_from_file = list()
    _scenario_test_ai = list()

    def __init__(self, mode=None, epochs=1, players=1):
        _TPI(self, locals())
        assert mode is not None, "Running mode is not specified"

        self.environment = Environment()
        self.scenario = list()
        self.mode = mode
        self.epochs = epochs
        self.players = players

    def run(self):
        _TPI(self, locals())
        assert self.scenario is not None, "Empty Scenario"
        for epoch in range(self.epochs):
            for action_set in self.scenario:
                assert type(action_set).__name__ is "list" or "tuple", "Action set should be a list."
                repeat = action_set[0]
                actions = action_set[1:]

                for action in actions:
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
                unit = list()
                unit.append(item[0])
                actions = item[1:]
                for action in actions:
                    if type(action).__name__ is "function" or "method":
                        unit.append((action, dict(is_test=True)))
                    else:
                        action[1]['is_test'] = True
                        unit.append((action[0], action[1]))

                return_value.append(unit)
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
        elif mode == "TESTING":
            raise NotImplementedError("NOT Implemented")
        elif mode == "LEARN_FROM_FILE":
            raise NotImplementedError("NOT Implemented")

    def act_get_players_data(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            raise NotImplementedError("ERROR")

    def act_run_ai_with_learn(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            raise NotImplementedError("ERROR")

    def act_ai_learn(self, is_test=False):
        if is_test is True:
            _TPI(self, locals())
        else:
            raise NotImplementedError("ERROR")