name = input("What is your name?: ")
print("The name length is",len(name))
print("The first letter of your name is:",name[0])
print("The first 3 letters of your name are:",name[0:3])
print("Now, the program will reverse your name...")
reverse = name [::-1]
print(reverse)
print("Finally, the program will congratulate you:")
congrats_word = "Congratulations"
print(congrats_word + " " + name)