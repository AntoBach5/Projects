money = int(input("Enter the amount of money you have: "))

while money > 0:
    cost = int(input("\nEnter the cost of what you are buying: "))
    money = money - cost
    if money <= 0:
        print("You don't have enough money")
        continue
    print(f"You've spent {cost}$, your current money is {money}")
    print("---")