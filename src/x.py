def draw_x_logo(size):
    for i in range(size):
        for j in range(size):
            if i == j:
                print("\\\\\\\\\\\\\\\\\\", end="")  # Backslash for one diagonal
            elif j == size - i - 1:
                print("//////", end="")  # Forward slash for the other diagonal
            else:
                print("-", end="")  # Dash for the background
        print()  # Move to the next line

# Example usage
draw_x_logo(20)  # Adjust size for a larger or smaller logo