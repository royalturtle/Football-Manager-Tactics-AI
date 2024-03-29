import argparse

from src.Agent import Agent
from src.constants.constant_networks import *
from src.constants.constant_modes import *
from src.constants.constant_game import ConstantGame


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--mode",
        default=available_modes[0],
        choices=available_modes,
        dest="mode",
        help="""Running mode of AI ["TACTICS", "MATCHES", "TEST_TACTICS", "TEST_MATCHES"]"""
    )
    parser.add_argument(
        "-a",
        "-ai",
        default="TestModel",
        choices=list(available_networks.keys()),
        dest="ai_model",
        help="""Select AI Models"""
    )
    parser.add_argument(
        "-e",
        "--epochs",
        default=1,
        type=int,
        dest="epochs",
        help="""Count of Epochs"""
    )

    args = parser.parse_args()

    agent = Agent(
        ai_name=args.ai_model,
        mode=args.mode,
        epochs=args.epochs,
        players=ConstantGame.count_teams()
    )
    agent.run()
