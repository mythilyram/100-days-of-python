#
print("Welcome to the tip calculator")
bill= float(input("What was the total bill? $"))
no_of_persons=int(input("How many people to split the bill? "))
tip_perc=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
amt = (bill+(tip_perc/100)*bill)/no_of_persons
amt_rounded=round(amt,1)
print("Each person should pay: $"+str(amt_rounded))


# Output
Welcome to the tip calculator
What was the total bill? $100
How many people to split the bill? 10
What percentage tip would you like to give? 10, 12, or 15? 10
Each person should pay: $11.0
