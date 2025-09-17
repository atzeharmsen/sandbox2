import xarray as xr
from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import pandas as pd


def match_grid_lifetime_emission(lifetime_data_path, emission_data_path):

    lifetime_data = xr.load_dataset(lifetime_data_path)

    emission_data = xr.load_dataset(emission_data_path)

    x = np.array(lifetime_data["Altitude"], dtype=float)  # independent variable
    x_newc = np.unique(np.concatenate([np.unique(emission_data["plev"].values), x]))
    x_newc = np.sort(x_newc)  # ensure monotonic ascending for interp1d

    # make sure x is sorted ascending
    order = np.argsort(x)
    x = x[order]
    plt.figure(figsize=(8, 5))
    stack = np.empty((0, len(x_newc)))
    # your arrays (replace with your variables)
    for index, latdeg in enumerate(lifetime_data["Latitude"].values):
        print(latdeg, index)
        # index = 0
        y = np.array(lifetime_data["tau_H2O"][:, index], dtype=float)  # dependent
        y = y[order]
        f_logy = interp1d(x, np.log(y), kind="linear", fill_value="extrapolate")
        y_c = np.exp(f_logy(x_newc))
        stack = np.vstack((stack, y_c))
        # Plot to compare
        plt.plot(x_newc, y_c, "--", label="linear in log(y)  (straight on semilogy)")
        plt.scatter(x_newc, y_c)
        plt.scatter(x, y, color="red", label="original points")

        plt.yscale("log")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
    plt.show()

    print(stack.shape)

    # Example matrix of shape (49,6)

    # Original x-coordinates of the columns
    x_original = np.array([-90, -37.5, 0, 45, 75, 90])

    # New x-coordinates for interpolation
    x_new = np.arange(-90, 91, 1)  # from -90 to 90 with step 1 (181 points)

    # Interpolated matrix
    interpolated_lifetime_data = np.zeros((stack.T.shape[0], len(x_new)))

    # Interpolate each row
    for i in range(stack.T.shape[0]):
        interpolated_lifetime_data[i, :] = np.interp(x_new, x_original, stack.T[i, :])

    print("Original shape:", stack.T.shape)
    print("Interpolated shape:", interpolated_lifetime_data.shape)

    ## Now we have interpolated lifetime data which is the pletzer data with more detail
    lifetime_df = pd.DataFrame(
        interpolated_lifetime_data, index=x_newc, columns=np.arange(-90, 91, 1)
    )

    emission_df = emission_data[["lat", "plev", "H2O"]].to_dataframe()

    # Group by unique (lat, plev) pairs and sum over all longitudes
    emission_df_altlat = emission_df.groupby(["lat", "plev"])["H2O"].sum().unstack()
    return lifetime_df, emission_df_altlat.T


def get_perturbation_mass(lifetime_df, emission_df_altlat):
    # Extract NumPy array and sorted coordinate values
    emis_lats = emission_df_altlat.columns.values  # 1-D array of latitudes
    emis_plevs = emission_df_altlat.index.values

    lifetime_df_sub = lifetime_df.loc[emis_plevs]
    lifetime_df_sub = lifetime_df_sub.loc[:, emis_lats]

    water_pert_df = (
        emission_df_altlat * lifetime_df_sub / 12
    )  # to convert from month to year
    tot = water_pert_df.sum(skipna=True).sum()
    print("emitted perturbation=", tot / 1e9, "Tg  Assuming steady state")
    return water_pert_df, tot


#%%

lifetime_data_path = (
    r"C:\Users\atzeh\PycharmProjects\OAC_Thesis\ATZE\dissertation_fig_7-9.nc"
)
emission_data_path = (
    r"C:\Users\atzeh\PycharmProjects\OAC_Thesis\ATZE\emi_inv_2020_DEPA.nc"
)

lifetime_df, emission_df_altlat = match_grid_lifetime_emission(
    lifetime_data_path, emission_data_path
)
water_pert_df, total_mass = get_perturbation_mass(lifetime_df, emission_df_altlat)
