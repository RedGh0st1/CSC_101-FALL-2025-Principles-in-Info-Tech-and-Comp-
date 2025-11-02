import time
# Write a program that answers this questions (What is your total?) using the input function
# Take the value entered and add 7% to the total
# Display the total and your name (your actual name)

my_question = "What is my total?"
print(my_question)
 
time.sleep(4)

responded = "how much did you pay?"
print(responded)

time.sleep(3)
paid = int(input()) 
print("you ok paid:", paid)

your_name = input("Whats your name: ")
total = paid + (paid * 7 / 100)

print("Ok,", your_name, "your total is:", + total)