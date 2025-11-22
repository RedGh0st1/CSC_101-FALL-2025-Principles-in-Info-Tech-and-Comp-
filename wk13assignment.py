# Instructions
# Answer must be submitted in a python file (.py at the end of the file)
# Create a function that takes three arguments
# argument 1 - will be the operation to perform as a string 
# + for addition
# - for subtraction
# + for addition
# * for multiplication
# argument 2 will be a value
# argument 3 will be another value
# function should look like perform_operation(operation, value1, value2)
# when the function is called with these arguments perform_operation("+", 4, 10), I would expect the function to return 14 as the result.
# You are required to use the return keyword
# This assignment is similar to an assignment in the past, but this time you will solve the problem using a function.



# create a function that takes three arguments name perfome_operation

def perform_operation(operation, value1, value2):

    # check if the operation is addition
    if operation == "+": return value1 + value2

    # check if the operation is subtraction
    elif operation == "-": return abs(value1 - value2)
    
    # check if the operation is division
    elif operation =="/":return value1/value2

    # check if the operation is multiplication
    elif operation == "*": return abs(value1 * value2)
    
  #  if the operation is not valid return "Invalid entry"
    else: return "Invalid entry"



print(perform_operation("+", 4, 10))
print(perform_operation("-", 4, 10))
print(perform_operation("*", 4, 10))
print(perform_operation("/", 5, 10))