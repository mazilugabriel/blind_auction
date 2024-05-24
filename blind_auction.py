programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }
#retrieving items from dictionary.
print(programming_dictionary["Bug"])

#adding new item to dictionary
programming_dictionary["Loop"] = "The action of doing somethin ove and over again."
print(programming_dictionary)

# #create new empty dictionary
empty_dictionary = {}
empty_dictionary["Loop"] = "The action of doing somethin ove and over again."
print(empty_dictionary["Loop"])

# #wipe an existing dictionary
empty_dictionary = {}
print(empty_dictionary)

# #edit an item in a dictionary
empty_dictionary["Loop"] = "different value"
print(empty_dictionary["Loop"])

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])