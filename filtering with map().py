numbers = list(input("Enter a list of numbers, separated by spaces: ").split())

def odd(n):
    if int(n) % 2 != 0:
        return n
    else:
        pass

def even(n):
    if int(n) % 2 == 0:
        return n
    else:
        pass

odds_from_list = list(map(odd, numbers))
evens_from_list = list(map(even, numbers))

print("Odd numbers... ",odds_from_list)
print("Even numbers... ",evens_from_list)

### Second excersise ###

fruits = ("apple", "kiwi", "strawberries", "watermelon", "pineapple")

capitalized_fruits = map(lambda fruit: fruit.capitalize(), fruits)

print(list(capitalized_fruits))