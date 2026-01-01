import processes
from utils.plot_utils import graph_processes
from utils.parsers import simulator_parser
import matplotlib.pyplot as plt

def main(args): 
    simulator = getattr(processes, args.simulator)
    sample_paths = simulator(args.T, args.dT, args.B)
    graph_processes(sample_paths, args.dT, f"{args.simulator.capitalize()} Process Sample Paths")
    plt.show()


if __name__ == "__main__":
    parser = simulator_parser()
    args = parser.parse_args()
    main(args)


