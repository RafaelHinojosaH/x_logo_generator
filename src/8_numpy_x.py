import numpy as np

size = 7
x = np.zeros((size, size), dtype=str)
x[:] = " "
np.fill_diagonal(x, "X")
np.fill_diagonal(np.fliplr(x), "X")

for row in x:
    print("".join(row))
