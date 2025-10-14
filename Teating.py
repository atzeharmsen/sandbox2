import xarray as xr
from matplotlib import pyplot as plt

import numpy as np

a = np.pi
import pandas as pd

df = pd.DataFrame()
import scipy as sp


# Re-run the fitting code (retrying).

import numpy as np
from scipy.integrate import odeint
from scipy.optimize import least_squares
import matplotlib.pyplot as plt

# --------------------------- User inputs (REPLACE THESE) ---------------------------
years = np.arange(1750, 2001)  # 1750..2000 inclusive
CH4_ppb = (
    700 + (1900 - 700) * ((years - years.min()) / (years.max() - years.min())) ** 1.5
)

import xarray as xr
import matplotlib.pyplot as plt

ch4_bg = r"C:\Users\atzeh\PycharmProjects\OAC_Thesis\repository\ch4_bg.nc"
xrds_ch4_bg = xr.load_dataset(ch4_bg)
# xrds_ch4_bg.data_vars["SSP5-8.5"].plot()
CH4_ppb = xrds_ch4_bg.data_vars["SSP5-8.5"][:251]

obs_intervals = [
    (1750, 2000, 229.0 + 1300),  # example: 5 Tg increase from 1750 to 2000
    (1950, 2000, 130.0 + 1300),  # example: 2 Tg increase from 1950 to 2000
    (1979, 2000, 49.0 + 1300),  # example: 0.8 Tg increase from 1979 to 2000
]

tau_CH4 = 8.6  # years; methane lifetime for conversion of burden -> oxidation flux.
fix_M0 = True
M0_fixed = 1300

ppb_to_Tg = 2.763  # Tg per ppb for global methane burden

CH4_burden_Tg = CH4_ppb * ppb_to_Tg

t_fine = np.linspace(years.min(), years.max(), int((years.max() - years.min()) * 4) + 1)
CH4_burden_fine = np.interp(t_fine, years, CH4_burden_Tg)


def integrate_M(tgrid, CH4_burden, f, tau_s, M0):
    S = f * CH4_burden / tau_CH4

    def dMdt(M, t_idx):
        S_t = np.interp(t_idx, tgrid, S)
        return S_t - M / tau_s

    M = odeint(lambda M, t: dMdt(M, t), M0, tgrid).flatten()
    return M


def modeled_delta_M_for_interval(tgrid, M_t, t0, t1):
    M0 = np.interp(t0, tgrid, M_t)
    M1 = np.interp(t1, tgrid, M_t)
    return M1 - M0


def residuals(params):
    log_f = params[0]
    log_tau_s = params[1]
    f = np.exp(log_f)
    tau_s = np.exp(log_tau_s)
    if fix_M0:
        M0 = M0_fixed
    else:
        M0 = params[2]
    M_t = integrate_M(t_fine, CH4_burden_fine, f, tau_s, M0)
    res = []
    for (t0, t1, obs_dM) in obs_intervals:
        mod_dM = modeled_delta_M_for_interval(t_fine, M_t, t0, t1)
        res.append(mod_dM - obs_dM)
    return np.array(res)


init_log_f = np.log(1e-3)
init_log_tau_s = np.log(2.0)
if fix_M0:
    x0 = np.array([init_log_f, init_log_tau_s])
else:
    x0 = np.array([init_log_f, init_log_tau_s, 50.0])

if fix_M0:
    lower = np.array([np.log(1e-8), np.log(0.1)])
    upper = np.array([np.log(1.0), np.log(100.0)])
else:
    lower = np.array([np.log(1e-8), np.log(0.1), 0.0])
    upper = np.array([np.log(1.0), np.log(100.0), 1e4])

result = least_squares(residuals, x0, bounds=(lower, upper), verbose=1)

f_fit = np.exp(result.x[0])
tau_s_fit = np.exp(result.x[1])
M0_fit = M0_fixed if fix_M0 else result.x[2]

print("Fitted parameters:")
print(f"  f (production factor) = {f_fit:.3e}")
print(f"  tau_s (SWV lifetime) = {tau_s_fit:.3f} years")
print(f"  M0 (initial SWV mass) = {M0_fit:.3f} Tg")

M_t_fit = integrate_M(t_fine, CH4_burden_fine, f_fit, tau_s_fit, M0_fit)

print("\nObserved vs modeled ΔM:")
for (t0, t1, obs_dM) in obs_intervals:
    mod_dM = modeled_delta_M_for_interval(t_fine, M_t_fit, t0, t1)
    print(
        f"  {t0}-{t1}: observed {obs_dM:.3f} Tg, modeled {mod_dM:.3f} Tg, diff {mod_dM-obs_dM:.3e} Tg"
    )

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(t_fine, CH4_burden_fine / ppb_to_Tg, label="CH4 (ppb, interp)")
ax1.set_xlabel("Year")
ax1.set_ylabel("CH4 (ppb)")
ax2 = ax1.twinx()
ax2.plot(t_fine, M_t_fit, label="Modeled SWV (Tg)", linestyle="--")
ax2.set_ylabel("SWV mass (Tg)")
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
plt.title("CH4 and modeled SWV mass (fitted)")
plt.grid(alpha=0.3)
plt.show()
