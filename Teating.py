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


### OLD CODE FROM BEFORE SUMMER
# def calc_stratospheric_ch4_loss(conc_ch4, lifetime_ch4 , mass_atm):
#     STRATOSPHERIC_LOSS_FACTOR = 0.08
#     mass_ch4 = mass_atm * conc_ch4 * (molar_mass_ch4 / molar_mass_air)
#     loss_ch4 = mass_ch4 / lifetime_ch4
#     stratospheric_loss_ch4 = loss_ch4 * STRATOSPHERIC_LOSS_FACTOR
#     return stratospheric_loss_ch4
#
#
# def calc_swv_mass(mass_stratospheric_loss_ch4):
#     parts_stratospheric_loss_ch4 =  mass_stratospheric_loss_ch4/molar_mass_ch4
#     parts_swv = parts_stratospheric_loss_ch4*2
#     mass_swv = parts_swv * molar_mass_h2o
#     return mass_swv
#

#
#
# # since 1750 to 2000 the ch4 concentrations go from 700 to 1750 ppbv from myhre and the background files
#
# def trial_run():
#     old_trial_conc_ch4 = 750 * 10**-9 # 750 ppbv
#     trial_lifetime_ch4 = 8 # yr
#     trial_mass_atm = 5.15 *10**18 #kg
#     old_trial_strat_ch4_loss = calc_stratospheric_ch4_loss(old_trial_conc_ch4, trial_lifetime_ch4, trial_mass_atm)
#     old_trial_mass_swv = calc_swv_mass(old_trial_strat_ch4_loss)
#
#     new_trial_conc_ch4 = 1750 * 10**-9 # 1750 ppbv
#     new_trial_strat_ch4_loss = calc_stratospheric_ch4_loss(new_trial_conc_ch4, trial_lifetime_ch4, trial_mass_atm)
#     new_trial_mass_swv = calc_swv_mass(new_trial_strat_ch4_loss)
#     return old_trial_mass_swv, new_trial_mass_swv
#
#
#
# old, new = trial_run()
# delta_swv_mass = new - old
# print(delta_swv_mass,"kg or ", delta_swv_mass*10**-9," Tg")
# # 64 Tg -> ~26mW/m2 (pletzer), 28 (grewe), myhre said 83...
