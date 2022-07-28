import numpy as np
import pandas as pd

table = pd.read_csv("dc_data/electron_mobility_diffusion.txt", delimiter="  ",engine="python")

p3 = 0.1 #torr

k = 1.38e-23 #J/K
T = 300 #K
NA = 6.022e23

p_Pa = p3*133.322 #Pascals

n_lin = p_Pa/(k*T) #m^-3

table['Mobility'] = table['Mobility'].apply(lambda x: x*n_lin)
table['Diffusion'] = table['Diffusion'].apply(lambda x: x*n_lin)

np.savetxt('dc_data/reduced_moments.txt', table.values, fmt='%.3e')