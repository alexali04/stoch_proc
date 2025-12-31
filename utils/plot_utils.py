import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def graph_processes(sample_funcs: np.ndarray, dT: float, title: str) -> plt.Figure:
    B = sample_funcs.shape[0]
    num_steps = sample_funcs.shape[1]

    time = np.arange(num_steps) * dT
    xlabel = "T"
    
    plt.figure(figsize=(12, 6))
    
    for i in range(B):
        plt.plot(time, sample_funcs[i, :], alpha=0.7, linewidth=1.5)
    

    legend_elements = plt.gca().get_legend_handles_labels()[0]
    legend_labels = plt.gca().get_legend_handles_labels()[1]
    legend_elements.append(Line2D([0], [0], linestyle='None', marker='None', label=f'dT = {dT}, T = {time[-1]}'))
    plt.legend(handles=legend_elements, loc='best', fontsize=9)
    

    
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel("W(t)", fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return plt.gcf()