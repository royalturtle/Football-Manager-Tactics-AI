import copy
from src.utils.TestPrinter import _TPI
from src.AIs.constant_modes import *
from src.AIs.data.environment import Environment


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
        self.is_testing_scenario = False

    def run(self, scenario):
        # _TPI(self, locals())
        assert scenario is not None, "Empty Scenario"
        assert type(scenario).__name__ is "list" or "tuple", "Action set should be a list."
        repeat = scenario[0]
        actions = scenario[1:]

        for _ in range(repeat):
            for action in actions:
                if (type(action).__name__ == "function") or (type(action).__name__ =="method"):
                    func = action
                    args = dict(is_test=self.is_testing_scenario)
                    func(**args)
                elif type(action[0]).__name__ == "int":
                    self.run(action)
                else:
                    func = action[0]
                    args = action[1]
                    args['is_test'] = self.is_testing_scenario
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
            self.is_testing_scenario = False
        elif mode == "MATCHES":
            assert len(self._scenario_matches) > 0, "Scenario of matches is empty."
            set_scenario(self, self._scenario_matches)
            self.is_testing_scenario = False
        elif mode == "TEST_TACTICS":
            assert len(self._scenario_tactics) > 0, "Scenario of tactics is empty."
            # test_actions: list = set_action_as_test(self._scenario_tactics)
            set_scenario(self, self._scenario_tactics)
            self.is_testing_scenario = True
        elif mode == "TEST_MATCHES":
            assert len(self._scenario_matches) > 0, "Scenario of matches is empty."
            # test_actions: list = set_action_as_test(self._scenario_matches)
            set_scenario(self, self._scenario_matches)
            self.is_testing_scenario = True
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