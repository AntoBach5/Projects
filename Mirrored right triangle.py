rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(rows - i):
        print("  ", end="")
    for k in range(i + 1):
        print("* ", end = "")
    print("")

# - for i in range(1, rows + 1):