import matplotlib.pyplot as plt
import numpy as np

y = np.random.randn(10,10)
plt.hist(y,100)
plt.show()