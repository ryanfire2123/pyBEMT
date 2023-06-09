import matplotlib.pyplot as pl
import pandas as pd
from math import pi

from pybemt.solver import Solver

s = Solver('test1.ini')

T, Q, P, section_df = s.run()
