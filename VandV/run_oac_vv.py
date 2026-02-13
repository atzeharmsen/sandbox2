# import sys and append to PATH using sys.path.append(`.../oac`)
import os
import openairclim as oac
import sys
import numpy as np

sys.path.append("../../openairclim")


# change directory to match current file
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

from pathlib import Path
import os

# Set working directory to project root (OAC_Thesis)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
os.chdir(PROJECT_ROOT)

print("Working directory set to:", os.getcwd())

# oac.run(r"C:\Users\atzeh\PycharmProjects\OAC_Thesis\ATZE\VandV\Lee.toml")

oac.run(r"C:\Users\atzeh\PycharmProjects\OAC_Thesis\example\example.toml")
