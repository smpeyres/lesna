import matplotlib.pyplot as plt 
import numpy as np

# H2 + OH -> H + H2O

def k1A(T):
    return 7.7e-18*np.exp(-2100/T)

Tg1A = np.linspace(245,300,50)

def k3C(T):
    return 3.6e-22*(T**(1.52))*np.exp(-1740/T)

Tg3C = np.linspace(250,1000,150)

def k3M(T):
    return 5.3e-22*(T**(1.47))*np.exp(-1761/T)

Tg3M = 300


fig = plt.figure()
plt.plot(Tg1A, k1A(Tg1A), label="[1A]")
plt.plot(Tg3C, k3C(Tg3C), label="[3C]")
plt.plot(Tg3M, k3M(Tg3M), marker='o', label="[3M]")
plt.title("H2 + OH -> H + H2O")
plt.ylabel("k (m^3/s)")
plt.xlabel("T (K)")
plt.yscale("log")
plt.legend()
plt.show()