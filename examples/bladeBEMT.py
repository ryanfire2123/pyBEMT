import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
from math import pi
from pybemt.solver import Solver


def verificationBEMT():
    global T
    props = ['CLARKY.ini',
             'GOE_408.ini',
             'GOE_450.ini',
             'NACA_4412.ini',
             'NACA_63815.ini',
             'NRELS814.ini']
    data = np.zeros((len(props), 3), dtype=object)
    for (i, prop) in enumerate(props):
        print("--------",prop,"--------")
        s = Solver(prop)

        T, Q, P, section_df = s.run()
        data[i] = [prop, T, Q]
        print(section_df)

    np.savetxt("/Users/ryan/Documents/GitHub/DSE-Needles-Eye-project/Propulsion/verificationData.csv", data, delimiter=",", fmt="%s")
    return data


verificationBEMT()

