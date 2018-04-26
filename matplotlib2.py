import matplotlib.pyplot as plt
import numpy as np

ages = np.random.randint(1, 100, size = 300)
range = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, range, rwidth=0.5, histtype='bar')
plt.title('Ages Distribution')
plt.show()