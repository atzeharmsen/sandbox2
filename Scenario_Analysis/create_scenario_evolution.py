from create_time_evolution_adapted import (
    create_time_normalization_xr,
    convert_xr_to_nc,
    plot_time_norm,
)

import pandas as pd
import numpy as np

# %% create a df from the data from GREWE 2021, https://doi.org/10.1038/s41467-021-24091-y

# Read the file with no header, then manually build one
df_raw = pd.read_excel(
    r"C:\Users\atzeh\OneDrive\Documenten\TU\MASTER\Thesis\Grewe_et_al_data_210322.xlsx",
    sheet_name="Fig.1 Emissions",
    header=None,
    skiprows=[2, 3],
)

# Combine first two rows into one header
new_header = df_raw.iloc[0] + "_" + df_raw.iloc[1].fillna("")
df = df_raw[2:].copy()
df.columns = new_header

# Reset index
df = df.reset_index(drop=True)

df.pop(np.nan)

CurTec_fuel = [
    16.26,
    16.90,
    17.57,
    18.27,
    19.00,
    19.76,
    20.56,
    21.39,
    22.25,
    23.16,
    24.10,
    25.08,
    26.11,
    27.18,
    28.29,
    29.46,
    30.67,
    31.94,
    33.26,
    34.64,
    36.09,
    37.59,
    39.16,
    40.79,
    42.50,
    44.28,
    46.14,
    48.08,
    50.10,
    52.21,
    54.41,
    56.71,
    63.08,
    67.57,
    69.71,
    74.65,
    80.47,
    84.73,
    95.34,
    106.18,
    107.28,
    108.42,
    108.82,
    111.53,
    117.80,
    123.93,
    129.46,
    139.35,
    147.06,
    150.49,
    158.02,
    151.39,
    155.68,
    154.70,
    163.93,
    172.58,
    183.62,
    191.04,
    191.90,
    200.89,
    214.48,
    204.79,
    206.56,
    210.15,
    238.19,
    253.97,
    265.71,
    283.06,
    284.15,
    276.37,
    293.27,
    307.21,
    321.23,
    337.41,
    356.04,
    381.12,
    407.52,
    437.94,
    473.40,
    498.10,
    522.39,
    546.60,
    570.11,
    592.66,
    613.93,
    633.64,
    652.90,
    672.37,
    692.02,
    711.85,
    731.83,
    752.56,
    773.38,
    794.28,
    815.23,
    836.20,
    856.70,
    876.96,
    896.91,
    916.54,
    935.79,
    954.64,
    972.96,
    990.70,
    1007.84,
    1024.31,
    1038.93,
    1053.25,
    1067.24,
    1080.89,
    1094.17,
    1113.09,
    1125.51,
    1137.98,
    1150.50,
    1163.05,
    1175.65,
    1188.29,
    1200.96,
    1213.67,
    1226.41,
    1239.19,
    1251.99,
    1264.83,
    1277.69,
    1290.58,
    1303.49,
    1316.42,
    1329.37,
    1342.34,
    1355.33,
    1368.32,
    1381.33,
    1394.35,
    1407.38,
    1420.41,
    1433.56,
    1446.72,
    1459.87,
    1473.03,
    1486.18,
    1499.33,
    1512.47,
    1525.60,
    1538.71,
    1551.82,
    1564.90,
    1577.97,
    1591.01,
    1604.03,
    1617.03,
    1630.00,
    1642.93,
    1655.83,
    1668.70,
    1681.53,
    1694.32,
    1707.06,
    1719.76,
    1732.41,
    1745.01,
]
df[
    "CurTec_Fuel"
] = CurTec_fuel  # hardcoded added from the different Grewe data sheet...

df = df.rename(columns={"Scenario_Quantity": "Year"})
# df = df[df["Year"] >= 2020].reset_index(drop=True)
df = df.apply(pd.to_numeric, errors="coerce")

print(df.head())
print(df.keys())

# %% Create the BAU evolution
SA_dict = {
    "CurTec": {
        "co2": "CurTec_CO2",
        "nox": "CurTec_NOx",
        "fuel": "CurTec_Fuel",
        "name": "GCurTec",
    },
    "BAU": {
        "co2": "BAU_CO2",
        "nox": "CORSIA_NOx Emission",
        "fuel": "BAU/CORSIA_Fuel",
        "name": "GBAU",
    },
    "FP2050": {
        "co2": "FP2050_CO2 Emission",
        "nox": "FP2050_NOx Emission",
        "fuel": "FP2050_Fuel",
        "name": "GFP2050",
    },
    "FP2050cont": {
        "co2": "FP2050-cont_CO2-Emission",
        "nox": "FP2050-cont_NOx Emission",
        "fuel": "FP2050-cont_Fuel",
        "name": "GFP2050cont",
    },
}
# fuel, co2, nox, name
NORM_TIME = df["Year"].values

for scenario in SA_dict.keys():
    print(scenario)
    FUEL_ARR = df[SA_dict[scenario]["fuel"]].values / 1e9
    EI_CO2_ARR = df[SA_dict[scenario]["co2"]] / 1e9 / FUEL_ARR
    EI_H2O_ARR = 1.25 * np.ones(
        len(NORM_TIME), dtype="float32"
    )  # TODO H2O not defined by Grewe scenarios
    EI_NOx_ARR = df[SA_dict[scenario]["nox"]] / 1e9 / FUEL_ARR
    DIS_PER_FUEL_ARR = df["All Scenarios_Flown km"] / FUEL_ARR / 1e9

    norm_ds = create_time_normalization_xr(
        time_arr=NORM_TIME,
        fuel_arr=FUEL_ARR,
        ei_co2_arr=EI_CO2_ARR,
        ei_h2o_arr=EI_H2O_ARR,
        ei_nox_arr=EI_NOx_ARR,
        dis_per_fuel_arr=DIS_PER_FUEL_ARR,
    )
    convert_xr_to_nc(
        norm_ds, SA_dict[scenario]["name"] + "_evo", "../Scenario_Analysis/evolution/"
    )
    plot_time_norm(norm_ds)
