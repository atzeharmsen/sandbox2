import tomli as tomllib  # use tomli for Python <3.11
import tomli_w
import copy


# Load the base TOML file
with open("GBAU.toml", "rb") as f:
    base_config = tomllib.load(f)


# Generate new TOML files
SSP_scenarios = ["SSP1-1.9", "SSP2-4.5", "SSP4-6.0", "SSP3-7.0"]
for ssp in SSP_scenarios:
    config = copy.deepcopy(base_config)
    config["output"]["dir"] = "results_GBAU_" + ssp.replace(".", "_") + "/"
    config["output"]["name"] = "GBAU_" + ssp.replace(".", "_")
    config["background"]["CO2"]["scenario"] = ssp
    config["background"]["CH4"]["scenario"] = ssp
    config["background"]["N2O"]["scenario"] = ssp
    # config["simulation"]["output_dir"] = f"results/run{i}"

    filename = f"GBAU_{ssp.replace('.', '_')}.toml"
    with open(filename, "wb") as f:
        tomli_w.dump(config, f)
