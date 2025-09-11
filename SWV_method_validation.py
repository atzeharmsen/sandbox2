
"""
In this file the method of calculating SWV_RF due to CH4 oxidation will be validated.
This is done by proving the Myhre plots contain linear behaviour and the griding is of minor importance
Also the conversion from SWv mass to SWV RF will be proven
"""
from openairclim.calc_swv import *
def validate_grid():

    myhre_2a_df = construct_myhre_2a_df()
    myhre_2b_df = construct_myhre_2b_df()
    myhre_2c_df = construct_myhre_2c_df()
    mass_a_list =[]
    mass_b_list =[]
    mass_c_list =[]

    for delta_h in [10.,100.,1000.]:
        for delta_deg in [0.1, 1., 10.]:
            heights = np.arange(0, 60000 + delta_h, delta_h)  # 0 to 60 km
            latitudes = np.arange(-85, 86, delta_deg)  # -85° to 85°
            print('\n\nvalue for different grids:\n delta_h=', delta_h,'\n delta_deg=', delta_deg)
            mass_a = get_total_mass(myhre_2a_df, heights, latitudes, delta_h, delta_deg)
            mass_b = get_total_mass(myhre_2b_df, heights, latitudes, delta_h, delta_deg)
            mass_c = get_total_mass(myhre_2c_df, heights, latitudes, delta_h, delta_deg)
            mass_a_list = mass_a_list + [mass_a]
            mass_b_list = mass_b_list + [mass_b]
            mass_c_list = mass_c_list + [mass_c]
    print('mass a: ',mass_a_list)
    print('mass b: ',mass_b_list)
    print('mass c: ',mass_c_list)
    percentage_diff_a = (max(mass_a_list) - min(mass_a_list))/min(mass_a_list)*100
    percentage_diff_b = (max(mass_b_list) - min(mass_b_list))/min(mass_b_list)*100
    percentage_diff_c = (max(mass_c_list) - min(mass_c_list))/min(mass_c_list)*100
    print('percentage difference: ',percentage_diff_a,'%')
    print('percentage difference: ',percentage_diff_b,'%')
    print('percentage difference: ',percentage_diff_c,'%')
    # If the deg is 10, than the value will be higher. It is not realistic to make that value that big



def proof_linearity_myhre(): #TODO not finished yet
    for cp_a in [60]:#[50,60,70,80]:
        myhre_2a_df = construct_myhre_2a_df(cp_a=cp_a)
        myhre_2b_df = construct_myhre_2b_df(cp_a=cp_a)
        myhre_2c_df = construct_myhre_2c_df(cp_a=cp_a)
        delta_h = 100. # m
        delta_deg = 1  # deg

        heights = np.arange(0, cp_a*1000 + delta_h, delta_h)  # 0 to 60 km
        latitudes = np.arange(-85, 86, delta_deg)  # -85° to 85°
        mass_a = get_total_mass(myhre_2a_df, heights, latitudes, delta_h, delta_deg, plot_data=True)
        mass_b = get_total_mass(myhre_2b_df, heights, latitudes, delta_h, delta_deg, plot_data=True)
        mass_c = get_total_mass(myhre_2c_df, heights, latitudes, delta_h, delta_deg, plot_data=True)
        print('mass a: ',mass_a)
        print('mass b: ',mass_b)
        print('mass c: ',mass_c)
        print(f"percentage difference between plots {cp_a}: ", (max(mass_a,mass_b,mass_c)-min(mass_a,mass_b,mass_c))/min(mass_a,mass_b,mass_c)*100,"%")

def proof_above_60km_there_is_marginal_gain():

    # there is a marginal gain of 2%, however not sure if this is the best way to estimate, with the 2 cornerpoints
    mass_a_list =[]
    mass_b_list =[]
    mass_c_list =[]
    for cp_a in [50,60,70,80]: # above 81025m ambiance.Atmosphere gives an error
        myhre_2a_df = construct_myhre_2a_df(cp_a = cp_a)
        myhre_2b_df = construct_myhre_2b_df(cp_a = cp_a)
        myhre_2c_df = construct_myhre_2c_df(cp_a = cp_a)
        delta_h = 100. # m
        delta_deg = 1  # deg

        heights = np.arange(0, cp_a*1000 + delta_h, delta_h)  # 0 to 60 km
        latitudes = np.arange(-85, 86, delta_deg)  # -85° to 85°
        mass_a = get_total_mass(myhre_2a_df, heights, latitudes, delta_h, delta_deg, plot_data=True)
        mass_b = get_total_mass(myhre_2b_df, heights, latitudes, delta_h, delta_deg)
        mass_c = get_total_mass(myhre_2c_df, heights, latitudes, delta_h, delta_deg)

        mass_a_list = mass_a_list + [mass_a]
        mass_b_list = mass_b_list + [mass_b]
        mass_c_list = mass_c_list + [mass_c]
    # print('mass a: ',mass_a_list)
    # print('mass b: ',mass_b_list)
    # print('mass c: ',mass_c_list)
    percentage_diff_a = (max(mass_a_list) - min(mass_a_list))/min(mass_a_list)*100
    percentage_diff_b = (max(mass_b_list) - min(mass_b_list))/min(mass_b_list)*100
    percentage_diff_c = (max(mass_c_list) - min(mass_c_list))/min(mass_c_list)*100
    print('percentage difference a: ',percentage_diff_a,'%')
    print('percentage difference b: ',percentage_diff_b,'%')
    print('percentage difference c: ',percentage_diff_c,'%')

# validate_grid()

proof_linearity_myhre()


# proof_above_60km_there_is_marginal_gain()





