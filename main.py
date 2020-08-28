import argparse

from src.Agent import Agent
from src.AIs.constant_networks import *
from src.AIs.constant_modes import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--mode",
        default="TEST_TACTICS",
        choices=available_modes,
        dest="mode",
        help="""Running mode of AI ["TACTICS", "MATCHES", "TEST_TACTICS", "TEST_MATCHES"]"""
    )
    parser.add_argument(
        "-a",
        "-ai",
        default="TestModel",
        choices=available_networks.keys(),
        dest="ai_model",
        help="""Select AI Models"""
    )
    args = parser.parse_args()

    agent = Agent(args.ai_model, args.mode)
    agent.run()
