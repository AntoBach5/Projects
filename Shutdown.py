def shutdown(decision):
    if deside == "yes" or deside == "Yes" or deside == "YES":
    
        if condition_1 == "yes" or condition_1 == "Yes" or condition_1 == "YES" and condition_2 == "yes" or condition_2 == "Yes" or condition_2 == "YES":
            print("shuting down")
        elif condition_1 == "no" or condition_1 == "No" or condition_1 == "NO" and condition_2 == "yes" or condition_2 == "Yes" or condition_2 == "YES":
            print("We could not shutdown because there is not enough battery")
        elif condition_1 == "yes" or condition_1 == "Yes" or condition_1 == "YES" and condition_2 == "no" or condition_2 == "No" or condition_2 == "NO":
            print("We could not shutdown because there is no internet connection")
        else:
            print("Invalid answer (yes or no)")
    else:
        print("Try again")

deside = str(input("Do you want to shut down the computer?: "))

condition_1 = str(input("Does your computer have +30 battery charge?: "))
condition_2 = str(input("Does your computer have internet connection?: "))

shutdown(deside)