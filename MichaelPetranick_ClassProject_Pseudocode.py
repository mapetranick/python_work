# CIS-245 Introduction to Programming
# Class Project: Week 4 - Pseudocode
# Create a Python Application which asks the user for their zip code or city.
# Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
# Display the weather forecast in a readable format to the user.
# Use comments within the application where appropriate in order to document what the program is doing.
# Use functions including a main function.
# Allow the user to run the program multiple times.
# Validate whether the user entered valid data.  If valid data isn’t presented notify the user.
# Use the Requests library in order to request data from the webservice.
# Use Python 3.
# Use try blocks when establishing connections to the webservice.  
# You must print a message to the user indicating whether or not the connection was successful.

#program start
start

#welcome message
message 

#ask to input zip code or city 
input 

#establish connection to webservice
Use try blocks
URL = http://openweathermap.org/
API = 83faacd04ddf3f23c56837e7ec97c12e

#if connection successful, continue to display weather forecast
display 
#if unsuccessful, ask to try again later 
print try again later
loop back to the input of city or zip 

#if valid data isn't presented, 
print ask user to check input 
loop back to the input of city or zip 

#if valid data is presented, ask if user would like to input another city or zip, or finish.
print would you like to lookup another location
#if yes, loop back to the city/cip input
loop back to the input of city or zip 
#if no, proceed to concluding message

#goodbye








