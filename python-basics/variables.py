# declaring variables
# names cannot start with number and use _ for two words
my_dogs = 2
print(my_dogs)

a = 5
print(a + a)

# checks what data type the variable is
print(type(a))

# Strings - they have indexing so you can slice
# The slice() function returns a slice object.
# slice(start, end, step)
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
# output ('d', 'e')
print(a[x]) 

# Arguments
# This function can be used to slice tuples, arrays and lists.

# The value of the start parameter (or None if not provided)

# The value of the stop parameter (or last index of sequence)

# The value of the step parameter (or None if not provided). It cannot be 0.

# All three must be of integer type.

print("I'm going on a run")

# len() finds the length, will also include white space
b = "hello world"
print(len(b))