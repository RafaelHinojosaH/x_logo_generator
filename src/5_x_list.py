size = 7
grid = [[" " for _ in range(size)] for _ in range(size)]

for i in range(size):
    grid[i][i] = "X"
    grid[i][size - i - 1] = "X"

for row in grid:
    print("".join(row))
