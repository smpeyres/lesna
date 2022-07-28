import numpy as np

eV = np.array([1e-2, 2.154e-2, 4.642e-2, 0.1, 0.2154, 0.4642, 1.0, 2.154, 4.642, 10.00])
Te = eV*(2/3)

# Ar from Phelps database, BOLSIG+ (0.01 - 10 eV Maxwellian, 10 points)
# I = 15.8 eV
# m3/s -> cm3/s

Ar_ki = np.array([0, 0, 0, 0, 0, 0, 0.1923e-25, 0.3345e-18, 0.2168e-15, 0.5631e-14])
Ar_ki = Ar_ki*1e6

# N2 from Phelps database, BOLSIG+ (0.01 - 10 eV Maxwellian, 10 points)
# I = 15.6 eV



# H2 from Phelps database, BOLSIG+ (0.01 - 10 eV Maxwellian, 10 points)
# I = 15.4 eV

H2_ki = np.array([0, 0, 0, 0, 0, 0, 0.1152e-24, 0.1948e-18, 0.9934e-16, 0.2266e-14])
H2_ki = H2_ki*1e6

