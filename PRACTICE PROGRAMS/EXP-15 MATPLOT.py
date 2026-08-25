import matplotlib.pyplot as plt

height = [150, 155, 160, 165, 170]
weight = [45, 50, 55, 60, 70]

plt.scatter(height, weight)

plt.title("Height vs Weight")
plt.xlabel("Height")
plt.ylabel("Weight")

plt.show()
