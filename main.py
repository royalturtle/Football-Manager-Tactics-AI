import argparse

from src.Agent import Agent
from src.AIs.constant_networks import *
from src.AIs.constant_modes import *


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
        choices=available_networks.keys()[0],
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
    parser.add_argument(
        "-p",
        "--players",
        default=1,
        type=int,
        dest="players",
        help="""Number of Players"""
    )

    args = parser.parse_args()

    agent = Agent(
        ai_name=args.ai_model,
        mode=args.mode,
        epochs=args.epochs,
        players=args.players
    )
    agent.run()
