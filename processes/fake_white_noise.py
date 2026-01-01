import numpy as np

def fake_white_noise(T: int, dT: float, B: int) -> np.ndarray:
    """
    T = total time
    dT = time step length
    B = batch size

    X_t ~ N(0, 1)
    """

    num_steps = int(T / dT)
    process = np.random.randn(B, num_steps)

    return process