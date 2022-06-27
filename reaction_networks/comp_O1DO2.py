import matplotlib.pyplot as plt 
import numpy as np

# O(1D) + O2 -> O(3P) + O2 
# Excitation/deexciation by molecular impact?

def S2(T):
    return 3.2e-17*np.exp(67/T)

Tg2 = np.linspace(200,350,15)

fig = plt.figure()
plt.plot(Tg2,S2(Tg2),label="[2]")
plt.yscale("log")
plt.legend()
plt.show()

fig = plt.figure()
plt.plot(600,4.1e-17,marker="o",label="[D]")
plt.yscale("log")
plt.legend()
plt.show()

fig = plt.figure()
plt.plot(Tg2,S2(Tg2),color="b")
plt.plot(600,4.1e-17,marker="o",color="r")
plt.yscale("log")
plt.show()