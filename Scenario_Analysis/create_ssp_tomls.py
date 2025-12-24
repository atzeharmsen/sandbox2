import tomli as tomllib  # use tomli for Python <3.11
import tomli_w
import copy


for scenario in ["GBAU", "GCurTec", "GFP2050", "GFP2050cont", "c2017"]:

    # Load the base TOML file
    with open(scenario + ".toml", "rb") as f:
        base_config = tomllib.load(f)

    # Generate new TOML files
    SSP_scenarios = [
        "SSP5-8.5"
    ]  # ["SSP1-1.9", "SSP2-4.5", "SSP4-6.0", "SSP3-7.0", "c17"]
    for ssp in SSP_scenarios:
        if ssp == "c17":
            config = copy.deepcopy(base_config)
            config["output"]["dir"] = f"results_{scenario}_" + ssp + "/"
            config["output"]["name"] = f"{scenario}_" + ssp
            config["background"]["dir"] = ""
            config["background"]["CO2"]["file"] = "bg_co2_c17.nc"
            config["background"]["CO2"]["scenario"] = "constant_2017"
            config["background"]["CH4"]["file"] = "bg_ch4_c17.nc"
            config["background"]["CH4"]["scenario"] = "constant_2017"
            config["background"]["N2O"]["file"] = "bg_n2o_c17.nc"
            config["background"]["N2O"]["scenario"] = "constant_2017"
            # config["simulation"]["output_dir"] = f"results/run{i}"

            filename = f"{scenario}_{ssp}.toml"
        else:
            config = copy.deepcopy(base_config)
            config["output"]["dir"] = (
                f"results_{scenario}_" + ssp.replace(".", "_") + "/"
            )
            config["output"]["name"] = f"{scenario}_" + ssp.replace(".", "_")
            config["background"]["CO2"]["scenario"] = ssp
            config["background"]["CH4"]["scenario"] = ssp
            config["background"]["N2O"]["scenario"] = ssp
            # config["simulation"]["output_dir"] = f"results/run{i}"

            filename = f"{scenario}_{ssp.replace('.', '_')}.toml"
        with open(filename, "wb") as f:
            tomli_w.dump(config, f)
