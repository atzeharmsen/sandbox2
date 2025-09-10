import xarray as xr
from matplotlib import pyplot as plt

# # Replace with your file path
file_path = r"C:\Users\atzeh\PycharmProjects\OAC_Thesis\example\input\rnd_inv_2020.nc"  # or .grib, .h5

xrds = xr.open_dataset(file_path)
# print(xrds)
print(xrds.attrs)
dimensios = xrds.dims


coords = xrds.coords

data_vars = xrds.data_vars
print(data_vars)

print(data_vars['H2O'].values)
xrds['H2O'].plot()
xrds['NOx'].plot()
xrds['CO2'].plot()
plt.show()
xrds['lon'].plot()
plt.show()


#
# ds = xr.open_dataset(file_path)
# print(ds)         # Text summary of the dataset
# ds.info()         # Optional: Show dataset info
#
# # Plot first variable if it’s 2D
# var = list(ds.data_vars)[0]
# ds[var].plot()
# print('hahahahah', var)


