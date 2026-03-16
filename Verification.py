try: 
    age = int(input("Enter your age: "))
    if age % 2 == 0:
        type_age = "even"
        print(f"Your age is {age} and it is an {type_age} number")
    else:
        type_age = "odd"
        print(f"Your age is {age} and it is an {type_age} number")
except ValueError as error1:
    print("Invalid input enter a number")