applePrice = 10
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1kg Apples on the cart.")
elif (budget - applePrice > 70):
    print("Its okay, you can buy")
else:
    print("Alexa, do not add Apples to the cart.")