# CIS-245: Intro to Programming
# Create a program that includes a dictionary of stocks.
# Your dictionary should include at least 10 ticker symbols.
# The key should be the stock ticker symbol and the value should be the current price of the stock.
# Ask the user to enter a ticker symbol.
# Your program will search the dictionary for the ticker symbol and then print the ticker symbol and the stock price.
# If the ticker symbol isn’t located print a message indicating that the ticker symbol wasn’t found.

price_stock = {'AMZN':3297, 'WMT':130, 'BAC':25, 'BRK.B':206, 'NVDA':485, 'DIS':128, 'MSFT':214, 'EPD':18, 'MCD':209, 'SBUX':77}

while True:
    stock_ticker = input('Please enter the stock ticker symbol(type exit to close): ')

    if stock_ticker == 'exit':
        print("Thank you. Have a nice day!")
        break
    
    if stock_ticker in price_stock.keys():
        print('The current price of ' + stock_ticker + ' stock is ' + str(price_stock[stock_ticker]) + ' dollars.')
    else:
        print("Data not found for ",stock_ticker)
    








    
 

    
    
    

