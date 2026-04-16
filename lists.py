numbers = [1, 50, 34, 4, 57, 12, 21, 11, 9, 78]
square_root = []

counter = 0

for item in numbers:
    result = item ** 0.5
    square_root.append(result)

for item in square_root:
    counter += 1
    if item % 2 == 0:
        print(f"Item number {counter} is even: {item}")
    else:
        print(f"Item number {counter} is odd: {item}")
