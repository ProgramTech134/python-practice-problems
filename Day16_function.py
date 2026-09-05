def greet_user(name , country ="pakistan"):
    result = f"wellcome {name} | from {country}"
    return result 
user_name = input("Enter your name : ")
# country = input("Enter your country : ")
answer = greet_user(user_name)
print(answer)
