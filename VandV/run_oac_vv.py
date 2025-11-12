# import sys and append to PATH using sys.path.append(`.../oac`)
import os
import openairclim as oac
import sys
import numpy as np

sys.path.append("../../openairclim")


# change directory to match current file
os.chdir(os.path.dirname(os.path.abspath(__file__)))


oac.run(r"C:\Users\atzeh\PycharmProjects\OAC_Thesis\ATZE\VandV\Lee.toml")
