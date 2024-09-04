def print_number_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "".join(str(j) for j in range(1, i + 1)))


print_number_triangle(int(input("Enter")))
