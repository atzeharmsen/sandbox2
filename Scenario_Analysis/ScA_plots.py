import matplotlib.pyplot as plt
import xarray as xr

# results
def run_outputs():

    scenarios = [
        "GBAU_SSP2-4_5",
        "GCurTec_SSP2-4_5",
        "GFP2050_SSP2-4_5",
        "GFP2050cont_SSP2-4_5",
    ]  # , "c2017_SSP2-4_5"]

    # SWV_RF = 1
    # CH4_RF = 1
    # SWV_conc = 1
    # ratio_RF = 1

    # NOx_species = ['PMO', 'CH4', 'SWV', 'O3']
    scenario_color = {
        "GCurTec_SSP2-4_5": "r",
        "GBAU_SSP1-1_9": "g",
        "GBAU_SSP2-4_5": "b",
        "GBAU_SSP3-7_0": "y",
        "GBAU_SSP4-6_0": "black",
        "GFP2050_SSP2-4_5": "grey",
        "GFP2050cont_SSP2-4_5": "purple",
        "c2017_SSP2-4_5": "green",
    }

    for scenario in scenarios:
        # if scenario != 'GFP2050':
        #     continue
        label = scenario.replace("G", "")
        first, second, rest = label.split("_", 2)
        label = f"{first}"
        ds_path = f"results_{scenario}/{scenario}.nc"
        data = xr.open_dataset(ds_path)
        metric = xr.open_dataset(f"results_{scenario}/{scenario}_metrics.nc")

        rf_SWV = data[f"RF_SWV"][0].values
        rf_CH4 = data[f"RF_CH4"][0].values
        try:
            ratio = rf_SWV / rf_CH4
        except RuntimeError:
            ratio = []
            for i in range(len(rf_SWV)):
                ratio[i] = rf_SWV[i] / rf_CH4[i]

        # plt.figure("CH4 SSP2-4_5")
        # plt.plot(
        #     data["time"].values,
        #     rf_CH4,
        #     label="CH4" + scenario,
        #     color=scenario_color[scenario],
        # )
        # plt.legend()
        # plt.title("CH4 RF SSP2-4_5")
        # plt.xlim([2010, 2100])
        # plt.xlabel("time [years]")
        # plt.ylabel(r"RF [W m$^{-2}$]")
        # plt.grid()

        plt.figure("SWV SSP2-4_5", figsize=(8, 6))
        plt.plot(
            data["time"].values,
            rf_SWV,
            label=label,
            color=scenario_color[scenario],
        )
        plt.legend()
        # plt.title("SWV RF SSP2-4_5")
        plt.xlim([2010, 2100])
        # plt.xlabel("time [years]")
        plt.ylabel(r"RF [W m$^{-2}$]", fontsize=14)
        plt.xlabel("Time [yr]", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(True)
        plt.savefig(f"scenarios_SWV_RF.png")

        plt.figure("ratio SSP2-4_5")
        plt.plot(
            data["time"].values,
            ratio,
            label=label,
            color=scenario_color[scenario],
        )
        plt.legend()
        # plt.title("ratios SSP2-4_5")
        plt.xlim([2010, 2100])
        plt.ylabel(r"Ratio [-]", fontsize=14)
        plt.xlabel("Time [yr]", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(True)
        plt.savefig(f"scenarios_Ratio.png")

        # GWP_SWV = []
        # GWP_tot = []
        # ATR_SWV = []
        # ATR_tot = []
        # for year in range(2000, 2080):
        #     # year =2000
        #     GWP_SWV.append(metric[f"AGWP_20_{year}"].values[-2])
        #     GWP_tot.append(metric[f"AGWP_20_{year}"].values[-1])
        #     ATR_SWV.append(metric[f"ATR_20_{year}"].values[-2])
        #     ATR_tot.append(metric[f"ATR_20_{year}"].values[-1])
        #     # print(year, GWP_SWV)
        # plt.figure("GWP SSP2-4_5")
        # plt.plot(
        #     range(2000, 2080), GWP_SWV, label=scenario, color=scenario_color[scenario]
        # )
        # plt.legend()
        # plt.title("GWP20 SSP2-4_5")
        # plt.xlim([2010, 2100])
        # plt.xlabel("time [years]")
        # plt.ylabel(r"GWP20 [-]")
        # plt.grid()
        #
        # plt.figure("ATR20 SSP2-4_5")
        # plt.plot(
        #     range(2000, 2080), ATR_SWV, label=scenario, color=scenario_color[scenario]
        # )
        # plt.legend()
        # plt.title("ATR20")
        # plt.xlim([2010, 2100])
        # plt.xlabel("time [years]")
        # plt.ylabel(r"ATR20 [-]")
        # plt.grid()

    # results
    #
    #
    #
    plt.show()
    return  # TODO Just fo skip al stuf below

    scenarios = [
        "GBAU_SSP2-4_5",
        "GBAU_SSP1-1_9",
        "GBAU_SSP3-7_0",
        "GBAU_SSP4-6_0",
        "GBAU_c17",
    ]

    # NOx_species = ['PMO', 'CH4', 'SWV', 'O3']
    scenario_color = {
        "GBAU_c17": "r",
        "GBAU_SSP1-1_9": "g",
        "GBAU_SSP2-4_5": "b",
        "GBAU_SSP3-7_0": "y",
        "GBAU_SSP4-6_0": "black",
        "GFP2050": "grey",
        "GFP2050cont": "purple",
        "c2017": "green",
    }

    for scenario in scenarios:
        # if scenario != 'GFP2050':
        #     continue
        ds_path = f"results_{scenario}/{scenario}.nc"
        data = xr.open_dataset(ds_path)
        metric = xr.open_dataset(f"results_{scenario}/{scenario}_metrics.nc")

        rf_SWV = data[f"RF_SWV"][0].values
        rf_CH4 = data[f"RF_CH4"][0].values
        try:
            ratio = rf_SWV / rf_CH4
        except RuntimeError:
            ratio = []
            for i in range(len(rf_SWV)):
                ratio[i] = rf_SWV[i] / rf_CH4[i]

        plt.figure("CH4 GBAU")
        plt.plot(
            data["time"].values,
            rf_CH4,
            label="CH4" + scenario,
            color=scenario_color[scenario],
        )
        plt.legend()
        plt.title("CH4 RF GBAU")
        plt.xlim([2010, 2100])
        plt.xlabel("time [years]")
        plt.ylabel(r"RF [W m$^{-2}$]")
        plt.grid()

        plt.figure("SWV GBAU")
        plt.plot(
            data["time"].values,
            rf_SWV,
            label="SWV" + scenario,
            color=scenario_color[scenario],
        )
        plt.legend()
        plt.title("SWV RF GBAU")
        plt.xlim([2010, 2100])
        plt.xlabel("time [years]")
        plt.ylabel(r"RF [W m$^{-2}$]")
        plt.grid()

        plt.figure("ratio GBAU")
        plt.plot(
            data["time"].values,
            ratio,
            label="ratio" + scenario,
            color=scenario_color[scenario],
        )
        plt.legend()
        plt.title("ratios GBAU")
        plt.xlim([2010, 2100])
        plt.xlabel("time [years]")
        plt.ylabel(r"[-]")
        plt.grid()

        GWP_SWV = []
        GWP_tot = []
        ATR_SWV = []
        ATR_tot = []
        for year in range(2000, 2080):
            # year =2000
            GWP_SWV.append(metric[f"AGWP_20_{year}"].values[-2])
            GWP_tot.append(metric[f"AGWP_20_{year}"].values[-1])
            ATR_SWV.append(metric[f"ATR_20_{year}"].values[-2])
            ATR_tot.append(metric[f"ATR_20_{year}"].values[-1])
            # print(year, GWP_SWV)
        plt.figure("GWP GBAU")
        plt.plot(
            range(2000, 2080), GWP_SWV, label=scenario, color=scenario_color[scenario]
        )
        plt.legend()
        plt.title("GWP GBAU")
        plt.xlim([2010, 2100])
        plt.xlabel("time [years]")
        plt.ylabel(r"GWP [-]")
        plt.grid()

        plt.figure("ATR GBAU")
        plt.plot(
            range(2000, 2080), ATR_SWV, label=scenario, color=scenario_color[scenario]
        )
        plt.legend()
        plt.title("ATR GBAU")
        plt.xlim([2010, 2100])
        plt.xlabel("time [years]")
        plt.ylabel(r"ATR [-]")
        plt.grid()

    #
    #
    #
    #

    # results

    scenarios = [
        "c2017_SSP2-4_5",
        # "c2017_SSP1-1_9",
        "c2017_SSP3-7_0",
        "c2017_SSP4-6_0",
        "c2017_c17",
    ]

    # NOx_species = ['PMO', 'CH4', 'SWV', 'O3']
    scenario_color = {
        "c2017_c17": "r",
        "c2017_SSP1-1_9": "g",
        "c2017_SSP2-4_5": "b",
        "c2017_SSP3-7_0": "y",
        "c2017_SSP4-6_0": "black",
        "GFP2050": "grey",
        "GFP2050cont": "purple",
        "c2017": "green",
    }

    for scenario in scenarios:
        # if scenario != 'GFP2050':
        #     continue
        ds_path = f"results_{scenario}/{scenario}.nc"
        data = xr.open_dataset(ds_path)
        metric = xr.open_dataset(f"results_{scenario}/{scenario}_metrics.nc")

        rf_SWV = data[f"RF_SWV"][0].values
        rf_CH4 = data[f"RF_CH4"][0].values
        try:
            ratio = rf_SWV / rf_CH4
        except RuntimeError:
            ratio = []
            for i in range(len(rf_SWV)):
                ratio[i] = rf_SWV[i] / rf_CH4[i]

        plt.figure("CH4 c2017")
        plt.plot(
            data["time"].values,
            rf_CH4,
            label="CH4" + scenario,
            color=scenario_color[scenario],
        )
        plt.legend()
        plt.title("CH4 RF c2017")
        plt.xlim([2010, 2100])
        plt.xlabel("time [years]")
        plt.ylabel(r"RF [W m$^{-2}$]")
        plt.grid(True)

        plt.figure("SWV c2017")
        plt.plot(
            data["time"].values,
            rf_SWV,
            label="SWV" + scenario,
            color=scenario_color[scenario],
        )
        plt.legend()
        plt.title("SWV RF c2017")
        plt.xlim([2010, 2100])
        plt.xlabel("time [years]")
        plt.ylabel(r"RF [W m$^{-2}$]")
        plt.grid(True)

        plt.figure("ratio c2017")
        plt.plot(
            data["time"].values,
            ratio,
            label="ratio" + scenario,
            color=scenario_color[scenario],
        )
        plt.legend()
        plt.title("ratios c2017")
        plt.xlim([2010, 2100])
        plt.xlabel("time [years]")
        plt.ylabel(r"[-]")
        plt.grid(True)

        GWP_SWV = []
        GWP_tot = []
        ATR_SWV = []
        ATR_tot = []
        for year in range(2000, 2080):
            # year =2000
            GWP_SWV.append(metric[f"AGWP_20_{year}"].values[-2])
            GWP_tot.append(metric[f"AGWP_20_{year}"].values[-1])
            ATR_SWV.append(metric[f"ATR_20_{year}"].values[-2])
            ATR_tot.append(metric[f"ATR_20_{year}"].values[-1])
            # print(year, GWP_SWV)
        plt.figure("GWP c2017")
        plt.plot(
            range(2000, 2080), GWP_SWV, label=scenario, color=scenario_color[scenario]
        )
        plt.legend()
        plt.title("GWP c2017")
        plt.xlim([2010, 2100])
        plt.xlabel("time [years]")
        plt.ylabel(r"GWP [-]")
        plt.grid(True)

        plt.figure("ATR c2017")
        plt.plot(
            range(2000, 2080), ATR_SWV, label=scenario, color=scenario_color[scenario]
        )
        plt.legend()
        plt.title("ATR c2017")
        plt.xlim([2010, 2100])
        plt.xlabel("time [years]")
        plt.ylabel(r"ATR[-]")
        plt.grid(True)

    plt.show()


def run_inputs():
    scenario_color = {
        "GCurTec_SSP2-4_5": "r",
        "GBAU_SSP1-1_9": "g",
        "GBAU_SSP2-4_5": "b",
        "GBAU_SSP3-7_0": "y",
        "GBAU_SSP4-6_0": "black",
        "GFP2050_SSP2-4_5": "grey",
        "GFP2050cont_SSP2-4_5": "purple",
        "c2017_SSP2-4_5": "green",
    }
    for scenario in ["GBAU", "GCurTec", "GFP2050", "GFP2050cont"]:
        ds_p = f"results_{scenario}/{scenario}.nc"
        ds = xr.open_dataset(ds_p)
        time = ds["time"][0]
        ch4 = ds["conc_CH4"][0]
        plt.figure("CH4", figsize=[8, 5])
        ds["conc_CH4"][0].plot(
            x="time",
            label=scenario.strip("G"),
            color=scenario_color[scenario + "_SSP2-4_5"],
        )

        plt.legend(loc="lower left")

        plt.legend()
        # plt.title("ratios SSP2-4_5")
        plt.xlim([2010, 2100])
        plt.ylabel(r"CH$_4$ Concentration [ppbv]", fontsize=14)
        plt.xlabel("Time [yr]", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        # plt.grid(True)
        plt.title("")
        plt.savefig(f"ch4_input_scen.png")
        # plt.figure('SWV')
        # ds['RF_SWV'][0].plot(x="time", label=scenario+ '_swv')
        # ds['RF_CH4'][0].plot(x="time", label=scenario + '_ch4', linestyle='--')
        # plt.legend()
    plt.grid(True)
    plt.show()


def run_combination_plot():
    # results
    scenarios = ["GBAU", "GCurTec", "GFP2050", "GFP2050cont", "c2017"]
    ssps = [
        "_SSP2-4_5",
        # "c2017_SSP1-1_9",
        "_SSP3-7_0",
        "_SSP4-6_0",
        "_c17",
    ]

    # NOx_species = ['PMO', 'CH4', 'SWV', 'O3']
    scenario_color = {
        "GCurTec": "r",
        "GBAU": "b",
        "GFP2050": "grey",
        "GFP2050cont": "purple",
        "c2017": "green",
    }
    style = {
        "_SSP2-4_5": "-",
        # "c2017_SSP1-1_9",
        "_SSP3-7_0": "--",
        "_SSP4-6_0": ":",
        "_c17": "-.",
    }

    for scenario in scenarios:
        for ssp in ssps:

            # if scenario != 'GFP2050':
            #     continue
            ds_path = f"results_{scenario+ssp}/{scenario+ssp}.nc"
            data = xr.open_dataset(ds_path)

            rf_SWV = data[f"RF_SWV"][0].values
            rf_CH4 = data[f"RF_CH4"][0].values
            conc_CH4 = data[f"conc_CH4"][0].values

            try:
                ratio = rf_SWV / rf_CH4
            except RuntimeError:
                ratio = []
                for i in range(len(rf_SWV)):
                    ratio[i] = rf_SWV[i] / rf_CH4[i]

            plt.figure("SWV")
            plt.plot(
                data["time"].values,
                rf_SWV,
                label="SWV" + scenario + ssp,
                color=scenario_color[scenario],
                linestyle=style[ssp],
            )
            plt.legend()
            plt.title("SWV RF SSP2-4_5")
            plt.xlim([2010, 2100])
            plt.xlabel("time [years]")
            plt.ylabel(r"RF [W m$^{-2}$]")
            plt.grid()

            plt.figure("ratio SSP2-4_5")
            plt.plot(
                data["time"].values,
                ratio,
                label=scenario + ssp,
                color=scenario_color[scenario],
                linestyle=style[ssp],
            )
            plt.legend()
            plt.title("ratios SSP2-4_5")
            plt.xlim([2010, 2100])
            plt.xlabel("time [years]")
            plt.ylabel(r"[-]")
            plt.grid()

            plt.figure("concentration")
            plt.plot(
                data["time"].values,
                conc_CH4,
                label=scenario + ssp,
                color=scenario_color[scenario],
                linestyle=style[ssp],
            )
            plt.legend()
            plt.title("concentration CH4")
            plt.xlim([2010, 2100])
            plt.xlabel("time [years]")
            plt.ylabel(r"[ppbv]")
            plt.grid()
    plt.show()


def make_backgroud_plot():
    ch4_bg = r"C:\Users\atzeh\PycharmProjects\OAC_Thesis\repository\ch4_bg.nc"
    xrds_ch4_bg = xr.load_dataset(ch4_bg)
    xrds_ch4_bg.data_vars["SSP1-1.9"].plot(label="SSP1-1.9")
    xrds_ch4_bg.data_vars["SSP2-4.5"].plot(label="SSP2-4.5")
    xrds_ch4_bg.data_vars["SSP3-7.0"].plot(label="SSP3-7.0")
    xrds_ch4_bg.data_vars["SSP4-6.0"].plot(label="SSP4-6.0")
    xrds_ch4_bg.data_vars["SSP5-8.5"].plot(label="SSP5-8.5")
    # q.plot()
    plt.xlim([1940, 2100])
    # plt.ylim([1700,1900])
    plt.ylabel(r"CH$_4$ [ppbv]", fontsize=14)
    plt.xlabel("Time [yr]", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    plt.legend()
    plt.show()


# run_combination_plot()
# make_backgroud_plot()
run_inputs()

# run_outputs()
