from processes.wiener import wiener
from utils.plot_utils import graph_processes
import matplotlib.pyplot as plt


def main():
    dT = 0.1
    T = 100
    simulated_processes = wiener(T=T, dT=dT, B=8)  
    graph_processes(simulated_processes, dT=dT, title="Wiener Process Sample Paths")
    plt.show()

if __name__ == "__main__":
    main()