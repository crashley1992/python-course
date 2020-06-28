# What is a List
# List is a collection of data that is ordered and changable. Duplicates are permited 

# give an example
my_list = ["apple", "banana", "cherry"]

# Loop through a List
for fruit in my_list:
    print(fruit + "list")

# What is a tuple
# Tuple is a collection of data that is ordered in immutable. Duplicates are permited

# give an example
my_tuple = ("apple", "banana", "cherry")

# Loop through a touple
for fruit in my_tuple:
    print(fruit + " tuple")

# What is a Set
# A set is a collection of data which is ordered and unindexed. No duplicate members 

# give an example
this_set = {"apple", "banana", "cherry"}

# Loop through a set
for fruit in this_set:
    print(fruit + " set")

# What is a Dictionary
# A collection which is unordered, changeable, and indexed. 

# give an example
my_dict = {
    "first_name": "Ashley",
    "last_name": "Clarke"
}

# Display last name of dictionary
print(my_dict["last_name"])

# Get first name Ashley from dictionary
name = my_dict["first_name"] = "Ashley"
print(name)