# Create a function that finds the word "pear" in the list below. Make sure to solve this problem with a for loop.
# fruits = ["apple", "orange", "banana", "pear"]
# def find_fruit(). Exit the loop once the item has been found. Print the "item found - fruit name".


fruits = ["apple", "orange", "banana", "pear"]

# create a function that finds the word "pear" from the above list
def find_fruit():

    # create for loop to iterate through each fruit in the list
    for  fruit in fruits:

        # check if the current fruits is a string "pear"
        if fruit == "pear":

            # print item found with the fruit name 
            print("item found:", fruit)
            
        # edge case if item not found
        # else:
        #     print("item not found")

# call the function
find_fruit()
