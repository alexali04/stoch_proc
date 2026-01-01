# TODO - migrate to Hydra

import argparse

def simulator_parser():
    parser = argparse.ArgumentParser(description="Simulator parser")
    parser.add_argument("--simulator", type=str, required=True, help="Simulator to use")
    parser.add_argument("--T", type=int, required=True, help="Total time")
    parser.add_argument("--dT", type=float, required=True, help="Time step length")
    parser.add_argument("--B", type=int, required=True, help="Batch size")
    return parser