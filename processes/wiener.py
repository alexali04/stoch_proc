import numpy as np


def wiener_simulator(T: int, dT: float, B: int) -> np.ndarray:
    """
    T = total time
    dT = time step length
    B = batch size

    returns vector of (B, int(T / dT) + 1)
    """

    process = np.zeros(B)
    num_steps = int(T / dT) + 1

    increments = np.sqrt(dT) * np.random.randn(B, num_steps - 1)  # increments: N(0, dT)
    process = np.cumsum(increments, axis=1)                    # sample path is sum of incremental samples
    process = np.concatenate((np.zeros((B, 1)), process), axis=1)  # intial condition W(0) = 0

    return process