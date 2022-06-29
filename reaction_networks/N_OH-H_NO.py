import matplotlib.pyplot as plt 
import numpy as np

# N + OH -> H + NO

def k3C(T):
    return 1.8e-16*(T**(-0.2))

Tg3C = np.linspace(100,1000,int((900/5)))

def k1M(T):
    return 3.8e-17*np.exp(85/T)

Tg1M = 400

def k2M(T):
    return 3.8e-17*np.exp(86/T)

Tg2M = 300


fig = plt.figure()
plt.plot(Tg3C, k3C(Tg3C), label="[3C]")
plt.plot(Tg1M, k1M(Tg1M), marker='o', label="[1M]")
plt.plot(Tg2M, k2M(Tg2M), marker='o', label="[2M]")
plt.title("N + OH -> H + NO")
plt.ylabel("k (m^3/s)")
plt.xlabel("T (K)")
plt.yscale("log")
plt.legend()
plt.show()