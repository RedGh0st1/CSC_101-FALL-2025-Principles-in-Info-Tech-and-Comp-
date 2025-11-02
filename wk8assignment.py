# You will ask three questions (1-3 below). Based on the answer from question 3, you will determine to add, subtract, divide or multiply question 1 and 2.


# Enter first value?
first_value = int(input("what is the first value? "))

# Enter second value?
second_value = int(input("What is the second value? "))

# What operation would you like to perform? 1 to add, 2 to subtract, 3 to divide, and 4 to multiply.
operation = int(input("What operation would you like to perfomr? 1 to add, 2 to subtract, 3 to divide, and 4 to multiply "))

# If the user doesn't choose 1, 2, 3, 4, print "incorrect entry" otherwise print the result
if operation == 1:
     addition_result = first_value + second_value
     print(addition_result)
elif operation == 2:
     subtraction_result = first_value - second_value
     print(subtraction_result)
elif operation == 3:
     division_result = first_value // second_value
     print(division_result)
elif operation == 4:
     multiply_result = first_value * second_value 
     print(multiply_result)
else:
     print("incorrect entry")