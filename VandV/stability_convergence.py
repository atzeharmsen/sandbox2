from matplotlib import pyplot as plt
from openairclim.calc_ch4 import calc_swv_mass_conc
from openairclim.calc_swv import *
import numpy as np


# Check of steady state
input_mat = [
    [0, 0, 0, 100, 100, 100, 100, 100, 100, 100],
    [200, 200, 200, 200, 200, 200, 200, 100, 100, 100, 100, 100, 100, 100],
]
for input in input_mat:

    m, c, d = calc_swv_mass_conc(input)
    if input[0] == 200:
        input = input[4:]
        m = m[4:]
    t = np.arange(0, len(input))

    plt.figure(figsize=(10, 6))
    (line1,) = plt.plot(t, input, marker="o", color="tab:blue", label="input")
    plt.ylim([0, max(input) * 1.1])
    plt.ylabel("CH4 change [ppbv]", color="tab:blue")
    plt.xlabel("time")
    plt.tick_params(axis="y", labelcolor="tab:blue")

    # Create second y-axis
    plt.twinx()  # This returns a second Axes instance implicitly used by plt

    # Second plot (right y-axis)
    (line2,) = plt.plot(t, m, color="tab:red", label="swv mass")
    plt.ylim([0, max(m) * 1.1])

    plt.ylabel("SWV mass [Tg]", color="tab:red")
    plt.tick_params(axis="y", labelcolor="tab:red")

    # Title
    # plt.title("stability/convergence")
    plt.legend([line1, line2], ["CH4", "SWV"])
    plt.tight_layout()
plt.show()
