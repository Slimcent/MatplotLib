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

# yPoints = np.array([3, 8, 1, 10])
#
# plt.plot(yPoints, 'o:r')
# plt.show()

# LineStyle
# yPoints = np.array([3, 8, 1, 10])
#
# plt.plot(yPoints, linestyle='dotted')
# plt.show()

# Multiple lines
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])
#
# plt.plot(y1)
# plt.plot(y2)
# plt.show()

# Labels
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.plot(x, y)
#
# plt.title("Sports Watch Data", loc='left')
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.show()

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# font1 = {'family': 'serif', 'color': 'blue', 'size': 20}  # Setting the font size
# font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
#
# plt.title("Sports Watch Data", fontdict=font1)
# plt.xlabel("Average Pulse", fontdict=font2)
# plt.ylabel("Calorie Burnage", fontdict=font2)
#
# plt.plot(x, y)
# plt.show()

# Adding grid
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.plot(x, y)
#
# plt.grid()
# plt.show()

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.plot(x, y)
#
# plt.grid(axis='x')  # specify to show x(vertical) grid lines
# plt.show()

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.plot(x, y)
#
# plt.grid(axis='y')  # specify to show x(vertical) grid lines
# plt.show()

# Display multiple plots
# plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(1, 2, 1)
# plt.plot(x, y)
# plt.title("SALES")  # plot one title
#
# # plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(1, 2, 2)
# plt.plot(x, y)
# plt.title("INCOME")  # plot two title
#
# plt.suptitle("MY SHOP")  # plot overall title
# plt.show()

# Draw two plots on top of each other
# plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(2, 1, 1)
# plt.plot(x, y)
#
# # plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(2, 1, 2)
# plt.plot(x, y)
#
# plt.show()

# Using Bar graph
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#
# plt.bar(x, y, color="red")
# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.barh(x, y, color="hotpink")  # Horizontal bars
# plt.show()

# Histogram
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
