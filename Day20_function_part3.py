#______________________________________________Question 1___________________________________________________ 
#                            Filter Even Numbers from a List

# Create a function named get_even that takes a list of numbers as an argument. 
# Using a loop, find all the even numbers from that list, store them in a new list,
# and return the new list. Finally, call the function by passing a list of numbers and print the result.

# _________________________________code1_____________________________________________________________________

# def get_even(list_number):
#     even_list = []
#     for i in range(0 , len(list_number)):
#         num = list_number[i]
#         if(num % 2 == 0):
#             even_list.append(num)
#     return even_list

# print(get_even([4 ,6 ,8 ,1 ,0 ,12]))

# ______________________________________Question 2____________________________________________________________

#                                   Factorial Calculator

# Write a function named calculate_factorial that takes a positive number (num) as an argument. 
# Using a loop, calculate the factorial of that number and return the final result. Finally, 
# call the function with a number and print the answer.

# _____________________________________code2___________________________________________________________________
# def calculate_factorial(num):
#     fact = 1 
#     for i in range(0 , num):
#         fact = fact *( num - i)
#     return fact
 
# print(calculate_factorial(5))

# _____________________________________Question 3_______________________________________________________________
#                                   Palindrome Checker

# Create a function named is_palindrome that takes a word (text) as an argument. 
# Check if the word reads the same forwards and backwards (such as "madam" or "radar").
# If it is a palindrome, return True; otherwise, return False.


# def is_palindrome(text):
#     palindrome = False 
#     r = text[ : : -1 ]
#     if(text == r):
#         palindrome = True 
#     return palindrome 

# print(is_palindrome("madam"))


# __________________________________________Question 4______________________________________________________________

def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"  
    
    for char in text:
        if char in vowels:
            count = count + 1
            
    return count


print(count_vowels("Hello World"))  
print(count_vowels("Python"))      


