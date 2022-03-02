'''
William Hellems-Moody
Program: Make Change
This program will compute the amount of change the user will get
back after they purchase an item. It will also determine the
exact number of each coin the user will receive based on the amount
of change available.
'''

# Constants
QUARTERS = 25
DIMES = 10
NICKELS = 5
PENNY = 1

# Determine the amount user has in wallet and round to 2 decimals
walletAmount = float(input("Enter the amount of money in wallet up to $1 (Only numbers!): "))

# check each condition to validate the user input
if walletAmount < 0:
    print("Money in wallet cannot be negative! Try Again...\nProgram Ended")
    exit()
elif walletAmount == 0:
    print("Sorry but you have no money to spend! Try Again...\nProgram Ended")
    exit()

# Obtain the cost of items from user & prompt user to check re-enter their input
costOfItem = float(input("Enter cost of item (Only numbers!): "))

# If input is negative, less than zero or equal to zero end program and try again
if costOfItem <= 0:
    print("Price of item cannot be negative, less than, or equal to zero! Try Again...\nProgram Ended")
    exit()
elif costOfItem > walletAmount:
    print("Price of item cannot be greater than wallet amount! Try Again...\nProgram Ended")
    exit()

# Show user the amount of money they spent on their item
print("Your items costs $", round(costOfItem,2))

# Calculate the items cost and convert to integer to compute number of coins received
changeDue = round((walletAmount - costOfItem), 2) * 100
changeAmount = int(changeDue)

# If user spends the exact amount in wallet end program based on condition being true
if changeDue == 0:
    print("You spent exactly $", walletAmount)
    print("No change necessary... Thanks for your purchase!")
    exit()

# First determine remainder of each coin based on change the amount of change given

# remainders for Quarters, Dimes, Nickels and Pennies using % and coin values as integer
remQuarters = changeAmount % 25
remDimes = remQuarters % 10
remNickels = remDimes % 5
numPennies = remDimes % 5

'''
Second determine number of each coin the user will receive: 
For quarters take difference in change amount and remaining quarters divided 
by the value of quarters, dimes take difference between remaining 
quarters and remaining dimes divided by number of dimes... use same steps for nickels and pennies.
'''

# Determine the number of Quarters, Dimes, Nickels and Pennies.
numQuarters = (changeAmount - remQuarters) // 25
numDimes = (remQuarters - remDimes) // 10
numNickels = (remDimes - remNickels) // 5

# Output to the user the value of change they will receive and number of each coin
print("You have received exactly: ")
print(numQuarters, "Quarter(s)", numDimes, "Dime(s)", numNickels, "Nickel(s)", numPennies, "Pennie(s)")

# Display the total amount of money the user has received back from their purchase
totalChange = changeDue / 100
print("Your change is: $", totalChange)
print("Thanks for your purchase!")
