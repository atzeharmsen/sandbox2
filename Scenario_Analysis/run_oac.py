"""Demonstration of OpenAirClim simulation run"""

# if you have not added the oac folder to your PATH, then you also need to
# import sys and append to PATH using sys.path.append(`.../oac`)
import os
import openairclim as oac
import sys
import numpy as np

sys.path.append("../../openairclim")

#%%
# create files
# from utils.create_time_evolution import (
#     create_time_scaling_xr,
#     convert_xr_to_nc,
#     plot_time_scaling,
#     create_time_normalization_xr,
#     plot_time_norm,
# )
#
# SCALING_TIME = np.arange(2020, 2200, 1)
#
# SCALING_ARR = np.ones(len(SCALING_TIME))
# for i in range(len(SCALING_TIME)):
#     SCALING_ARR[i] = SCALING_ARR[i - 1] * 1.02
# SCALING_ARR = SCALING_ARR.astype("float32")
# print(SCALING_ARR)
# scaling_ds = create_time_scaling_xr(SCALING_TIME, SCALING_ARR)
# convert_xr_to_nc(
#     scaling_ds,
#     "time_scaling_2percentgrowthperyear",
#     out_path=r"C:/Users/atzeh/PycharmProjects/OAC_Thesis/ATZE/Scenario_Analysis/",
# )
# plot_time_scaling(SCALING_TIME, SCALING_ARR)
# norm_ds = create_time_normalization_xr(
#     NORM_TIME, FUEL_ARR, EI_CO2_ARR, EI_H2O_ARR, DIS_PER_FUEL_ARR
# )
# convert_xr_to_nc(norm_ds, "time_norm_examplexxxxxxxxxxx")
# plot_time_norm(norm_ds)


#%% RUN
# change directory to match current file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for scenario in [
    "\GBAU_SSP1-1_9",
    "\GBAU_SSP2-4_5",
    "\GBAU_SSP3-7_0",
    "\GBAU_SSP4-6_0",
]:
    # for scenario in ["\GBAU", "\GCurTec", "\GFP2050", "\GFP2050cont"]:
    oac.run(
        r"C:\Users\atzeh\PycharmProjects\OAC_Thesis\ATZE\Scenario_Analysis"
        + scenario
        + ".toml"
    )
