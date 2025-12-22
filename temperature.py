temp = float(input("Enter the current temperature in celsius (C)"))
if temp >= 30 and temp <= 50:
    print("The temperature is good to just wear a t-shirt and shorts")
elif temp < 30 and temp >= 15:
    print("The temperature is neutral, you should wear a thin pullover as well as shorts")
elif temp < 15 and temp >= 5:
    print("The temperature is pretty cold outside, better wear a jacket and trousers")
elif temp < 5:
    print("Outside is freezing, wear lots of layers of clothes")
else:
    print("I cannot understand that input, make sure that the temperature you entered is between -50 - 50")