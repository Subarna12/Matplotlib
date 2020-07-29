import matplotlib.pyplot as plt
import numpy as np

d = {'a':25, 'b':45, 'c':52}

for i,key in enumerate(d):
    plt.bar(i,d[key])

plt.xticks([0,1,2],['A-bar','B-bar','C-bar'])
#plt.xticks([0,1,2],d.keys())

plt.show()