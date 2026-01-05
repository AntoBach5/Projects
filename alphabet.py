user_enter = input("Enter a character of any type: ")
if ((user_enter >= "A" and user_enter <= "Z")) or ((user_enter >= "a" and user_enter <= "z")):
    print("The character you've input is a letter")
    if ((user_enter >= "A" and user_enter <= "Z")):
        print("Specifically, your letter is Higher case")
    else:
        print("Specifically, your letter is Lower case")
else:
    print("The character you've input is not a letter")