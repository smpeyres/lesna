import matplotlib.pyplot as plt 
import numpy as np

# N + O2 -> O + NO


def k3C(T):
    return 9.7e-21*(T**(1.01))*np.exp(-3120/T)

Tg3C = np.linspace(250,1000,144)

def k1P_1(T):
    return 4.2e-18*np.exp(-3220/T)

Tg1P_1 = np.linspace(200,300,20)

def k1P_2(T):
    return 1.1e-20*T*np.exp(-3150/T)

Tg1P_2 = np.linspace(300,500,40)

def k1M(T):
    return 4.4e-18*np.exp(-3220/T)

# [1M] and [2M] use same k, but are at diff temps

Tg1M = 400
Tg2M = 300


fig = plt.figure()
plt.plot(Tg3C, k3C(Tg3C), label="[3C]")
plt.plot(Tg1P_1, k1P_1(Tg1P_1), label="[1P]")
plt.plot(Tg1P_2, k1P_2(Tg1P_2), color="C1")
plt.plot(Tg1M, k1M(Tg1M),marker='o',label="[1M]")
plt.plot(Tg2M, k1M(Tg2M),marker='o',label="[2M]")
plt.title("N + O2 -> O + NO")
plt.ylabel("k (m^3/s)")
plt.xlabel("T (K)")
plt.yscale("log")
plt.legend()
plt.show()