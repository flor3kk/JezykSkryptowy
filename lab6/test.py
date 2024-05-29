
import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 5.0, 0.15)
t2 = np.arange(0.0, 5.0, 0.01)
t3 = np.arange(0, 10, 0.2)
t4 = np.arange(-10, 5, 1)

plt.figure()
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(223)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.subplot(224)
plt.plot(t3, [i**2 for i in t3])

plt.subplot(222)
plt.plot(t4, np.tan(1/3*np.pi*t4))
plt.show()