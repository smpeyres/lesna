import matplotlib.pyplot as plt 
import numpy as np

# H + HO2 -> OH + OH

def k1A(T):
    return 7.2e-17*(T/T)

Tg1A = np.linspace(245,300,11)

def k3C(T):
    return 7.4e-16*np.exp(-700/T)

Tg3C = np.linspace(250,1000,150)


fig = plt.figure()
plt.plot(Tg1A, k1A(Tg1A), label="[1A]")
plt.plot(Tg3C, k3C(Tg3C), label="[3C]")
plt.title("H + HO2 -> OH + OH")
plt.ylabel("k (m^3/s)")
plt.xlabel("T (K)")
plt.yscale("log")
plt.legend()
plt.show()