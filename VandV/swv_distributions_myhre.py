from openairclim.calc_ch4 import calc_swv_mass_conc
from openairclim.calc_swv import *
import xarray as xr
import matplotlib.pyplot as plt

ch4_bg = r"C:\Users\atzeh\PycharmProjects\OAC_Thesis\repository\ch4_bg.nc"
xrds_ch4_bg = xr.load_dataset(ch4_bg)

ch4_1750 = xrds_ch4_bg.data_vars["SSP5-8.5"][1750 - 1750].values

ch4_1946 = xrds_ch4_bg.data_vars["SSP5-8.5"][1946 - 1750].values
ch4_1947 = xrds_ch4_bg.data_vars["SSP5-8.5"][1947 - 1750].values
ch4_1948 = xrds_ch4_bg.data_vars["SSP5-8.5"][1948 - 1750].values
ch4_1949 = xrds_ch4_bg.data_vars["SSP5-8.5"][1949 - 1750].values
ch4_1950 = xrds_ch4_bg.data_vars["SSP5-8.5"][1950 - 1750].values

ch4_1975 = xrds_ch4_bg.data_vars["SSP5-8.5"][1975 - 1750].values
ch4_1976 = xrds_ch4_bg.data_vars["SSP5-8.5"][1976 - 1750].values
ch4_1977 = xrds_ch4_bg.data_vars["SSP5-8.5"][1977 - 1750].values
ch4_1978 = xrds_ch4_bg.data_vars["SSP5-8.5"][1978 - 1750].values
ch4_1979 = xrds_ch4_bg.data_vars["SSP5-8.5"][1979 - 1750].values

# ch4_1995 = xrds_ch4_bg.data_vars['SSP5-8.5'][1995-1750].values
ch4_1996 = xrds_ch4_bg.data_vars["SSP5-8.5"][1996 - 1750].values
ch4_1997 = xrds_ch4_bg.data_vars["SSP5-8.5"][1997 - 1750].values
ch4_1998 = xrds_ch4_bg.data_vars["SSP5-8.5"][1998 - 1750].values
ch4_1999 = xrds_ch4_bg.data_vars["SSP5-8.5"][1999 - 1750].values
ch4_2000 = xrds_ch4_bg.data_vars["SSP5-8.5"][2000 - 1750].values


delta_mass_1750, _, swv_distribution_1750 = calc_swv_mass_conc(
    [ch4_1750, ch4_1750, ch4_1750, ch4_1750, ch4_1750]
)
delta_mass_1950, _, swv_distribution_1950 = calc_swv_mass_conc(
    [ch4_1946, ch4_1947, ch4_1948, ch4_1949, ch4_1950]
)
delta_mass_1979, _, swv_distribution_1979 = calc_swv_mass_conc(
    [ch4_1975, ch4_1976, ch4_1977, ch4_1978, ch4_1979]
)
delta_mass_2000, _, swv_distribution_2000 = calc_swv_mass_conc(
    [ch4_1996, ch4_1997, ch4_1998, ch4_1999, ch4_2000]
)
print(delta_mass_1750)
print(delta_mass_1950)
print(delta_mass_1979)
print(delta_mass_2000)

A = delta_mass_2000[-1] - delta_mass_1750[-1]
B = delta_mass_2000[-1] - delta_mass_1950[-1]
C = delta_mass_2000[-1] - delta_mass_1979[-1]
print(A, B, C)


#%% PLOTS %%#
import matplotlib.image as mpimg

delta_h = 100.0  # height increment in meters
delta_deg = 1.0  # latitude increment
heights = np.arange(0, 60000 + delta_h, delta_h)  # 0 to 60 km
latitudes = np.arange(-85, 85, delta_deg)

# Load your background image
img = mpimg.imread(r"myhre2a.png")  # or .jpg, .tif, etc.

# Create the plot
fig, ax = plt.subplots()

# Show the image as the background
ax.imshow(
    img, extent=[-87, 87, 0, 65000], aspect="auto"
)  # adjust extent to match your data coordinates

ax.levels = np.arange(0.0, 2.0, 0.2)
ax.contours = plt.contour(
    latitudes,
    heights,
    (swv_distribution_2000 - swv_distribution_1750) / 1000,
    levels=ax.levels,
    colors="green",
    linestyles="dashed",
)
plt.clabel(ax.contours, inline=True, fontsize=12, fmt="%.1f")
plt.xlabel("Latitude (deg)")
plt.ylabel("Altitude (m)")
plt.title("swv_distribution")
plt.tight_layout()
plt.savefig("swv_distribution_a.png")
plt.show()


img = mpimg.imread(r"myhre2b.png")  # or .jpg, .tif, etc.

# Create the plot
fig, ax = plt.subplots()

# Show the image as the background
ax.imshow(
    img, extent=[-87, 87, 0, 65000], aspect="auto"
)  # adjust extent to match your data coordinates

ax.levels = np.arange(0.0, 2.0, 0.2)
ax.contours = plt.contour(
    latitudes,
    heights,
    (swv_distribution_2000 - swv_distribution_1950) / 1000,
    levels=ax.levels,
    colors="green",
    linestyles="dashed",
)
plt.clabel(ax.contours, inline=True, fontsize=12, fmt="%.1f")
plt.xlabel("Latitude (deg)")
plt.ylabel("Altitude (m)")
plt.title("swv_distribution")
plt.tight_layout()
plt.savefig("swv_distribution_b.png")
plt.show()


# Load your background image
img = mpimg.imread(r"myhre2c.png")  # or .jpg, .tif, etc.

# Create the plot
fig, ax = plt.subplots()

# Show the image as the background
ax.imshow(
    img, extent=[-87, 87, 0, 65000], aspect="auto"
)  # adjust extent to match your data coordinates

ax.levels = np.arange(0.0, 1.0, 0.1)
ax.contours = plt.contour(
    latitudes,
    heights,
    (swv_distribution_2000 - swv_distribution_1979) / 1000,
    levels=ax.levels,
    colors="green",
    linestyles="dashed",
)
plt.clabel(ax.contours, inline=True, fontsize=12, fmt="%.1f")
plt.xlabel("Latitude (deg)")
plt.ylabel("Altitude (m)")
plt.title("swv_distribution")
plt.tight_layout()
plt.savefig("swv_distribution_c.png")
plt.show()
