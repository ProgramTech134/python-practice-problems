# 1. Write a program to store seven fruits in a list entered by the user 

fruits = []

for i in range(1 , 8):
    fruit = input("Enter fruit name :")
    fruits.append(fruit)

print("This is the list of fruits :")
print(fruits)


# 2. Write a program to accept marks of 6 students and display them in a sorted manner.


marks =[]

for i in range(1, 7):
    mark = int(input("Enter mark :"))
    marks.append(mark)

marks.sort()
print("Marks of student")
print(marks)


# 3  Write a program to sum a list with 4 numbers.
numbers = []
sum = 0 

for i in range(1 ,5):
   number = int(input("Enter number :"))
   numbers.append(number)
   sum = sum + number 

print("sum of numbers :" , sum)