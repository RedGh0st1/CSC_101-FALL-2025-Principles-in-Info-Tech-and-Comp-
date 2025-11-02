



# USERNAME = "user1"
USERNAME = "user1"

# PASSWORD = "password1"
PASSWORD = "password1"

# What is your user name?
user_name = input("What is your user name? ")

# What is your password?
user_name_password = input("What is your password? ")

# What is your age?
user_age = int(input("What is your age? "))

# If the user name and password are incorrect, display a message that says - Your credentials are not valid
if user_name != USERNAME and user_name_password != PASSWORD:
    print("Your credentials are not valid")

# If both user name and password are correct, ask question 3
elif user_name == USERNAME and user_name_password == PASSWORD:

# If the answer to question 3 is eighteen and greater, display a message that says - You're considered an adult
    if user_age >= 18:
        print("You're considered an adult")
# If the answer to question 3 is less than eighteen, display a message that says - you're not considered an adult
    else:
        print("you're not considered an adult")   
# MAKE SURE to use the constants above