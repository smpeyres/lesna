import matplotlib.pyplot as plt 
import numpy as np

# N+ + NO -> NO+ + N 
# Charge exchange of nitrogen ion with nitrous oxide

def S1(T):
    return 1.90e-15*(T/T)

Tg1 = np.linspace(100,1000,4)

fig = plt.figure()
plt.plot(Tg1,S1(Tg1),label="[1]")
plt.yscale("log")
plt.legend()
plt.show()

fig = plt.figure()
plt.plot(300,4.72e-16,marker="o",label="[C]")
plt.yscale("log")
plt.legend()
plt.show()

fig = plt.figure()
plt.plot(Tg1,S1(Tg1),color="b")
plt.plot(300,4.72e-16,marker="o",color="r")
plt.yscale("log")
plt.show()