print("Enter fruits you like (in singular)")
enter1 = str(input("Enter first fruit: ").lower())
enter2 = str(input("Enter second fruit: ").lower())
enter3 = str(input("Enter third fruit: ").lower())

fruits_in_the_fridge = {
    "apple", "kiwi", "strawberries", "grapes", "watermelon", "pineapple"
    }

entered_fruits = {enter1, enter2, enter3}

print("From the fruits that you've entered, ")
print(entered_fruits.difference(fruits_in_the_fridge))

print("this are some that can go in the fridge: ")
print(entered_fruits.intersection(fruits_in_the_fridge))