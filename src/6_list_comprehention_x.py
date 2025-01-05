size = 7
grid = [
    "".join("X" if i == j or i + j == size - 1 else " " for j in range(size))
    for i in range(size)
]

print("\n".join(grid))
