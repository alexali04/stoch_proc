import numpy as np


def wiener(T: int, dT: float, B: int) -> np.ndarray:
    """
    T = total time
    dT = time step length
    B = batch size

    returns vector of (B, int(T / dT) + 1)

    X_{t + dT} - X_t ~ N(0, dT)
    X(0) = 0
    """

    num_steps = int(T / dT)

    increments = np.sqrt(dT) * np.random.randn(B, num_steps)  # increments: N(0, dT)
    process = np.cumsum(increments, axis=1)                    # sample path is sum of incremental samples
    process = np.concatenate((np.zeros((B, 1)), process), axis=1)  # intial condition W(0) = 0

    return process