
# _____________________________________code1______________________________________________________________________
# Question 2: Addition Function with Return
# Create a function named add_numbers. This function should take two arguments 
# (num1 and num2), calculate their sum, and return the result.

# Then, call this function, store the returned answer in a variable, and print it.


def Addition(num1 , num2):
    add = num1 + num2
    return add 

result = Addition(5 ,10)
print(result)

# _________________________________code2__________________________________________________________________________
# Question 3: Even or Odd Checker
# Create a function named check_even_odd. This function should take one number as an argument.
# If the number is even, print "Even number", and if it is odd, print "Odd number".

# Test this function by calling it with different numbers.


def check_even_odd(num1):
    
    if(num1%2 ==0):
        print("Even")
    else:
        print("odd")


num1 = int(input("Enter num1 :"))
check_even_odd(num1)

# ____________________________________________________code3_______________________________________________________

# Question 4: Function with Default Parameter
# Create a function named describe_pet. This function should take two parameters: pet_name and animal_type. Set the default value of animal_type to "dog".

# The function should print: "I have a [animal_type] named [pet_name]."

# Call this function twice: once by passing only the pet's name, and once by passing both values.


def describe_pet(pet_name ,animal_type = "dog"):
    print(f"I Have a {animal_type} named {pet_name} .")

describe_pet("shaomi")


#____________________________________________________________code_4________________________________________________

# Question 5: Finding the Maximum of Three Numbers
# Create a function named find_max that takes three numbers (a, b, and c) as arguments.
# This function should return the largest number among the three.

# Then, call this function and print the result.

def find_max(a , b ,c):
    
    if a > b and a > c :
        return a
    
    elif b > a and b > c :
        print("b is max")
        max = b
    else : 
        return c
    

print(find_max(1 , 4 ,7))