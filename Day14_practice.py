#                         ___________________________________________________________________________
#                         _____________________Problem Statement (Question)__________________________
# Problem Statement:
# Create a Python program capable of greeting the user with
# "Good Morning", "Good Afternoon", "Good Evening", or "Good Night" 
# by automatically fetching the current hour from the system using the time module.


import time  # Importing the time module to access system clock

# Fetching the current hour (0-23) from the system and converting it to an integer
hour = int(time.strftime("%H"))

# Checking the time ranges to print the correct greeting
if 5 <= hour < 12:
    print("Good morning")  # From 5:00 AM to 11:59 AM

elif 12 <= hour < 17:
    print("Good afternoon")  # From 12:00 PM to 4:59 PM

elif 17 <= hour < 21:
    print("Good evening")  # From 5:00 PM to 8:59 PM

else:
    print("Good Night")  # From 9:00 PM to 4:59 AM


