# Program Statement: Advanced Smart Calculator
# Create a smart calculator program. Take an input from the user. Use a match-case statement to handle different types of inputs and situations:

# If the input is "+"  or "-" or "*" or "/", print: "This is a valid mathematical operator."

# If the input is exactly 0 (integer or string "0"), print: "This is zero, it can cause division-by-zero errors."

# If the input is a boolean value True or False, print: "This is a Boolean data type."

# If the input is any other number (like 5, 22, etc.), print: "This is a standard number."

# If the input is anything else (Default case), print: "Unknown text or complex input!"

#________________________________solution________________________________________________
something_is = input("Enter something")

match something_is :
    case "+" | "-" | "*" | "/" :
        print("This is a valid mathematical operator")
    case "0" :
        print("This is a zero it can causes devision")
    case "true"  | "false":
        print("This is a boolen data type") 
    case _ if something_is.isdigit() :
        print ("This is a standard number")
    case _ :
        print("unkown text or complex input")