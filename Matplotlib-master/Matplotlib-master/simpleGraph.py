import matplotlib.pyplot as plt

# plt.plot([1,2,3,4,5,100])
# plt.show()

xValues = [1,2,3,4,5,100]
plt.plot(xValues,[i**2 for i in xValues])
plt.show()