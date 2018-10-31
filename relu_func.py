import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

x = np.arange(-10, 10, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 10.1)
plt.show()