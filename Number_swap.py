number_1 = 3
number_2 = 2
number_3 = 1

print(number_1, number_2, number_3)

temp_var = 0

temp_var = number_3
number_3 = number_2
number_2 = number_1
number_1 = temp_var

print(number_1, number_2, number_3)