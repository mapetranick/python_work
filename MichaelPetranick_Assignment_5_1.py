# CIS-245 Intro to Programming - Week 5
# Write a program that uses a while loop to determine how long it takes for an investment to double at a given interest rate.
# The input will be an annualized interest rate and the initial investment amount.
# The output is the number of years it takes an investment to double.

print("Welcome, this program will determine how long it take for an investment to double at a given interest rate. ")

rate = input("What is the annual interest rate? ")
investment = 1000
years = 0
total = investment

while total <= investment * 2:
    total = total + (total * float(rate)) / 100
    years = years + 1

print("Your investment will double in " + str(years) + " years at an interest rate of " + str(rate) + "%.")



