
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 11, 1)
y = x**2

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='--', color='red')
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Line Graph of y = x^2")
plt.grid(True)
plt.show()
