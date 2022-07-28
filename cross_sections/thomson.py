import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


ep = 8.854e-12
el = 1.6e-19

def sig(E,I):
    A = 16*(np.pi**2)*(ep**2)
    B = np.pi*(el**2)/E
    C = 5/(3*I) - 1/E - (2*I)/(3*(E**2))
    return B*C/A

e_vals = np.geomspace(4.3,1000,20)
result = sig(e_vals,4.209)

df = pd.DataFrame()

df['Energy (eV)']=pd.Series(e_vals)
df['Cross Section (m2)']=pd.Series(result)

print(df)



# fig = plt.figure()
# plt.plot(e_vals,sig(e_vals,4.209))
# plt.xscale("log")
# plt.xlabel("Electron Energy (eV)")
# plt.yscale("log")
# plt.ylabel("Ionization Cross Section (m2)")
# plt.show()
