import matplotlib.pyplot as plt
import matplotlib

op = matplotlib.markers.MarkerStyle(fillstyle='none')
cl = matplotlib.markers.MarkerStyle()

plt.plot([-7, 2], [0, 0], color='blue')
plt.plot([2, 3], [1 / 10, 1 / 10], color='blue')
plt.plot([3, 5], [2 / 10, 2 / 10], color='blue')
plt.plot([5, 7], [1, 1], color='blue')
plt.scatter(2, 0, facecolors='none', edgecolors='blue')
plt.scatter(2, 1/10, facecolors='blue', edgecolors='blue')
plt.scatter(3, 1/10, facecolors='none', edgecolors='blue')
plt.scatter(3, 2/10, facecolors='blue', edgecolors='blue')
plt.scatter(5, 2/10, facecolors='none', edgecolors='blue')
plt.scatter(5, 1, facecolors='blue', edgecolors='blue')
plt.savefig('2.pdf', format='pdf')
