# Take the list above and create the 2 functions. Make sure to loop and don't just use if on the list.
# 1.  Create a function called modify_animal_names(list) and uppercase the first letter of each word. And add underscore your initials. For example the above list should be modified to match ['Ankylosaurus_ah', 'Carnotaurus_ah', 'Spinosaurus_ah', 'Trex_ah', ]. My initials are ah and ah should be your initials, not ah.
# 2.  Create a function called find_replace_name(list, name) that finds the word "Spinosaurus_ah" and replace it with your name. DO NOT use the replace function. Do this manually by looping (for loop).
# All functions you were asked to create must take the list as an argument. These functions do not have a return value. Your functions will modify the list of items. You can always print the list to ensure your code modified the list in each function. Do not use built in functions to do this.

# 1. function to modify animal names
dinosaurs = ['ankylosaurus', 'carnotaurus', 'spinosaurus', 'trex', ]
my_initials = "_ln" 
uppercased_dict = {'a': 'A', 'b': 'B','c': 'C','s': 'S','t': 'T',}

def modify_animal_names(dinosaurs):
    for i in range(len(dinosaurs)):
       dinosaurs[i] = uppercased_dict[dinosaurs[i][0]] + dinosaurs[i][1:] + my_initials
    print(dinosaurs)

modify_animal_names(dinosaurs)



#2. function to find and replace the "Spinosaurus_ah" with your name

def find_replace_name(dinosaurs, name):
    for i in range(len(dinosaurs)):
       if dinosaurs[i] == "Spinosaurus_ln": dinosaurs[i] = name
    print(dinosaurs)

find_replace_name(dinosaurs, "Lennie Nurse")
