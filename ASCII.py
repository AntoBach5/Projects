import time, os

while True:
    enter = input("Enter any character, only 1: ")
    if type(enter) is str and len(enter) == 1:
        print("Valid input!")
        break
    else:
        print("Invalid input, enter ONE character")
print("---------")
ascii_value = ord(enter)

print(f"Character: {enter}")
print(f"ASCII value: {ascii_value}")
time.sleep(1.5)
print("---------")

if ascii_value >= 65 and ascii_value <= 90:
    print("The character you've inputed is uppercase")
elif ascii_value >= 97 and ascii_value <= 122:
    print("The chracter you've inputed is lowercase")
elif ascii_value >= 48 and ascii_value <= 57:
    print("The character you've inputed is a digit")
elif ascii_value == 32:
    print("The character you've inputed is Space Bar")
else:
    print("The character you've inputed is a special character")
