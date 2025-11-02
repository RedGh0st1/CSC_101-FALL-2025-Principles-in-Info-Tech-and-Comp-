# Answer must be submitted in a python file (.py at the end of the file)
# Make sure you understand the list data structure -  https://www.w3schools.com/python/python_lists.asp
# Add (total) all the number in the list (below) using a while loop.
# numbers = [10,20,35,40,60,100]

numbers = [10, 20, 35, 40, 60, 100]

#created a variable to keep track of the index 
index = 0

# created a variable to keep track of the total
total = 0

# created a while loop to iterate through the list if the index is less than or equal to the length of the list
while index <= len(numbers) - 1:

    # added the current number in the list to the total variable
    total += numbers[index]
    
    # incremented the index by 1
    index +=1 

# printed the total
print(total)