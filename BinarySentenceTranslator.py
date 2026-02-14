import time

dec_num = int(input("Enter a number and the program will convert it to Binary!: "))
binary_result = ""

if dec_num == 0:
    binary_result = "0"

while dec_num > 0:    
    remainder = dec_num % 2
    binary_result = str(remainder) + binary_result 
    dec_num = dec_num // 2

print(f"The binary representation of {dec_num} is...")
time.sleep(1)
print(binary_result)