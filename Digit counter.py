user_num = int(input("Enter a number and the program will find the number of digits: "))

temp = user_num
sum = 0

while temp >0:
    digit = temp%10
    sum = sum + 1
    temp = temp // 10

print(f"The number of digits is {sum}")
