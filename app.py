#Green Christmas Tree
def print_christmas_tree(height):
    for i in range(height):
        spaces = " " * (height - i - 1)
        stars = "\033[92m" + "*" * (2 * i + 1) + "\033[0m"  # ANSI code for green color
        print(spaces + stars)

    # Print tree trunk
    trunk_spaces = " " * (height - 1)
    print(trunk_spaces + "| |")


tree_height = 5  # Adjust the height as needed

print_christmas_tree(tree_height)
