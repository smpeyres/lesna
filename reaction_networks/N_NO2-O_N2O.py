import matplotlib.pyplot as plt 
import numpy as np

# N + NO2 -> O + N2O

def k1P(T):
    return 3e-18*(T/T)

Tg1P = np.linspace(200,500,int((300/5)))

def k1M(T):
    return 2.4e-18*((T/300)**0.5)

Tg1M = 400

def k2M(T):
    return 3.4e-18*(T/T)

Tg2M = 300


fig = plt.figure()
plt.plot(Tg1P, k1P(Tg1P), label="[1P]")
plt.plot(Tg1M, k1M(Tg1M), marker='o', label="[1M]")
plt.plot(Tg2M, k2M(Tg2M), marker='o', label="[2M]")
plt.title("N + NO2 -> O + N2O")
plt.ylabel("k (m^3/s)")
plt.xlabel("T (K)")
plt.yscale("log")
plt.legend()
plt.show()