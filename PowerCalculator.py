enter = int(input("Enter the Base number: "))
power = int(input("Enter the Exponential number: "))

result = 0

for i in range(power):
    result = enter * power

print("The number {0} to the power of {1} is...{2}".format(enter, power, result))