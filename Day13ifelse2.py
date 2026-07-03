# 🛍️ Problem: The Discount Checker
# Imagine you are making a billing system for a clothing store. The store has a very simple rule for a discount:

# If a customer's total shopping bill is more than $50, they get a $10 discount.

# Else (if the bill is $50 or less), they get no discount ($0).

# Your program should calculate and print the final amount the customer has to pay.

Bill = int(input("Enter the total amount of your bill :"))
print("your bill is :" , Bill)

if(Bill>50):
    print(" you get a $10 discount.")

else :
   print("you get no discount")
   print("your final  bill is :" , Bill)
   

