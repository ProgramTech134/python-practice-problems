#____________________________________________________Question 1__________________________________________________________

#_____________________________________Sum of Arbitrary Arguments (*args)_________________________________________________

# Write a function named sum_all that uses *args instead of a normal parameter, 
# allowing the user to pass as many numbers as they want. The function should add
# (sum) all those numbers together and return the total result. Finally, call the 
# function with multiple numbers and print the answer.

# __________________________________________code 1 _______________________________________________________________________

def sum_all(*arg):
    total = 0
    for i in arg :
     total = total + i 
    return total 

print(sum_all(3, 5 ,7 ,9 ,2, 9))
# _______________________________________________question 2___________________________________________________________________
                            
# Write a function named find_maximum that uses *args to accept any number of arguments (such as 5, 12, 3, 9, 20). 
# Use a loop and logic to find and return the largest (maximum) number among them. Finally, call the function with 
# multiple numbers and print the result.

# _________________________________________________code 2 ______________________________________________________________________


def find_maximum(*arg):
    max = 0 
    for i in arg:
        if(i > max):
            max = i
    return max 

print(find_maximum(8 ,2 ,9 ,3 ,6 ,4 ,10))


#___________________________________________________Question 2 ___________________________________________________________________

#                                          Multiply All Numbers using *args

# Task: Write a function named multiply_all that uses *args to accept multiple numbers. 
# The function should multiply all those numbers together and return the total product
# (for example, calling multiply_all(2, 3, 4) should return 24). Finally, test the function by printing the output.

# ______________________________________________code 3 _____________________________________________________________________________

def multi_all(*arg):
    product = 1 
    for i in arg:
        product = product * i 
    return product 

print(multi_all(5 ,10 ,2))






