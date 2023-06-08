 # -*- coding: utf-8 -*-

import matplotlib.pyplot as pl
import pandas as pd
from math import pi

from pybemt.solver import Solver

s = Solver('propeller.ini')

df, sections = s.run_sweep('v_inf', 20, 1, 44.0)

df_exp = pd.read_csv("propeller_data.csv", delimiter=' ')

ax = df.plot(x='J', y='eta', legend=None) 
df_exp.plot(x='J', y='eta', style='C0o',ax=ax, legend=None)
pl.legend((r'BEMT, $\eta$', r'Exp, $\eta$'),loc='center left')

pl.ylabel(r'$\eta$')
ax2 = ax.twinx()
pl.ylabel(r'$C_P, C_T$')

df.plot(x='J', y='CP', style='C1-',ax=ax2, legend=None) 
df_exp.plot(x='J',y='CP',style='C1o',ax=ax2, legend=None)

df.plot(x='J', y='CT', style='C2-',ax=ax2, legend=None) 
df_exp.plot(x='J',y='CT',style='C2o',ax=ax2, legend=None)


pl.legend((r'BEMT, $C_P$', r'Exp, $C_P$',
           r'BEMT, $C_T$', r'Exp, $C_T$'), loc='center right')

pl.show()

