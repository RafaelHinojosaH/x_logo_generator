def print_x(size):
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print("X", end="")
            else:
                print(" ", end="")
        print()

print_x(20)
