#  Project Title: Electricity Bill Calculator
# Problem Statement:
# Write a Python program that asks the user for two
#  inputs:
# Customer Name (String)
# Total Units Consumed (Integer)
# Calculation:
# The price for one unit is Rs. 25.

# Calculate the total bill using this formula: totalbill = unit * 25
# Output:
# Display a message on the screen in this exact format:

# "Dear [Name], your total electricity bill is Rs. [Amount]." 

a =  input("Customer name :")
b =  input("Total unit consumed :")

oneunit = 25
Totalbill = oneunit*int(b)

print(Totalbill)
print("Dear",a,"your total electricity bill is RS:",Totalbill)
