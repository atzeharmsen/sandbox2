import os
from pathlib import Path
import xarray as xr


from openairclim.calc_h2 import run_case

working_dir = Path(os.path.dirname(os.path.abspath(os.getcwd()))).as_posix()

result = run_case(
    wd=working_dir,
    scenario="ssp126",
    start_year=2035,
    t_mid=2060,
    m_adp=0.27,
    f_app=0.0300,
    f_del=0.0133,
    f_prod=0.0178,
    kd=0.38,
)
print(result)
