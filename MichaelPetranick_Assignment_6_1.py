# CIS 240 Introduction to Programming
# Assignment 6.1
# Write a program that uses a function to convert miles to kilometers.
# Your program should prompt the user for the number of miles driven then call a function which converts miles to kilometers.
# Check and validate all user input and incorporate Try/Except block(s).
# The program should then display the total miles and the kilometers.

name = input("Hello, what is your name? ")
print("Hello, " + name + "!")

miles = input("How many miles have you driven? ")

while True:
    try:
        def convert_distance(miles):
            km = miles * 1.609
            return km
        result = convert_distance(float(miles))
        print("You have driven " + str(miles) + " miles.")
        print("You have driven " + str(result) + " kilometers.")
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
        break
        
    
    

