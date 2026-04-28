values_dictionary = {"we": 1, "all": 2, "love": 2, "codingal": 1, "because": 4 }
print("Original dictionary: "+ str(values_dictionary))

x = int(input("Enter the value that you want to check the number of occurences: "))
result = 0

for item in values_dictionary:
    if values_dictionary[item] == x:
        result = result + 1

print(f"The number of items in the dictionary with value {x} is: {result}")