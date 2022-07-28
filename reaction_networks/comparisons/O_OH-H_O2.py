import matplotlib.pyplot as plt 
import numpy as np

# O + OH -> H + O2

def k1A(T):
    return 2.4e-17*np.exp(110/T)

Tg1A = np.linspace(150,500,int(350/5))

def k3C(T):
    return 2.0e-16*(T**(-0.352))*np.exp(113/T)

Tg3C = np.linspace(250,1000,144)

def k1M(T):
    return 2.3e-17*np.exp(110/T)

# [1M] and [2M] use same k, but are at diff temps

Tg1M = 400
Tg2M = 300

def k3M(T):
    return 6e-17*(T**(-0.186))*np.exp(-154/T)

Tg3M = 300


fig = plt.figure()
plt.plot(Tg1A, k1A(Tg1A), label="[1A]")
plt.plot(Tg3C, k3C(Tg3C), label="[3C]")
plt.plot(Tg1M, k1M(Tg1M),marker='o',label="[1M]")
plt.plot(Tg2M, k1M(Tg2M),marker='o',label="[2M]")
plt.plot(Tg3M, k3M(Tg3M),marker='o',label="[3M]")
plt.title("O + OH -> H + O2")
plt.ylabel("k (m^3/s)")
plt.xlabel("T (K)")
plt.yscale("log")
plt.legend()
plt.show()