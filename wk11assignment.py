# Make sure you understand the list data structure -  https://www.w3schools.com/python/python_lists.asp

# Add (total) all the number in the list (below) excluding even numbers using the for loop.

numbers = [10,21,30,40,53,60,100,1,3]

# created a variable to keep track of the total
total = 0

# created a for loop to iterate through each odd number in the list
for num in numbers:

    # if the number is odd
    if num % 2 == 1:
       
       # added the current odd number in the list to the total variable
       total+=num

# printed the total
print(total)

