import matplotlib.pyplot as plt

size = 5
x_coords = list(range(size))
y_coords = list(range(size))
y_coords_reverse = list(reversed(range(size)))

plt.scatter(x_coords, y_coords, color="red")
plt.scatter(x_coords, y_coords_reverse, color="blue")
plt.show()
