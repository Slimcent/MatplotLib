import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# matplotlib.use('Agg')

# xPoints = np.array([0, 6])
# yPoints = np.array([0, 250])
#
# plt.plot(xPoints, yPoints)
# plt.show()
#
# # Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

# Using dots
# xPoints = np.array([1, 8])
# yPoints = np.array([3, 10])
#
# plt.plot(xPoints, yPoints, 'o')
# plt.show()

# Having many points
# xPoints = np.array([1, 2, 6, 8])
# yPoints = np.array([3, 8, 1, 10])
# plt.plot(xPoints, yPoints)
# plt.show()

# Using dots on many points

# xPoints = np.array([1, 2, 6, 8])
# yPoints = np.array([3, 8, 1, 10])
# plt.plot(xPoints, yPoints, 'o')
# plt.show()

# Default value of x
# yPoints = np.array([3, 8, 1, 10, 5, 7])  # Not specifying x values will make it to have default values of x of 1,2,3,4,5
#
# plt.plot(yPoints)
# plt.show()
#
# # Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

# Using markers
# yPoints = np.array([3, 8, 1, 10])
#
# plt.plot(yPoints, marker='o')
# plt.show()

yPoints = np.array([3, 8, 1, 10])

plt.plot(yPoints, 'o:r')
plt.show()
