# CIS 240 Introduction to Programming
# Assignment 4.1
# Calculate the cost of installing fiber optic cable at a cost of .87 per ft for a company.
# Bulk discount .80 greater than 100 feet
# Bulk discount .70 greater than 250 feet
# Bulk discount .50 greater than 500 feet

print("Hello!")
print("What is the name of your company?")

name = input()

print("The cost of fiber optic cable per foot is 87 cents.")

print("If you order 100 feet or more, you will receive a bulk discount of 80 cents per foot.")

print("If you order 250 or more, you will receive a bulk discount of 70 cents per foot.")

print("If you order 500 feet or more, you will receive a bulk discount of 50 per foot.")

print("How much fiber optic cable would you like to purchase (in feet)?")

amount = int(input())

if amount < 100:
    price = amount * .87
elif amount < 250:
    price = amount * .80
elif amount < 500:
    price = amount * .70
elif amount >= 500:
    price = amount * .50

print("The cost of " + str(name) + "'s" + " order is $" + str(price) + " dollars")

print("Thank you and have a nice day.")




