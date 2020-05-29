# String Indexing/Slicing

my_string = "Hello World"

print(my_string)

# negative elements pull from the end of the string
print(my_string[-1])

new_string = 'abcdefghijk'

# grabs everything from c to the end of index
print(new_string[2:])

# grabs everything from begining to c index but not including c
print(new_string[:2])

# gets range from index position 3 to 6
print(new_string[3:6])

print(new_string[0:3])

# the third parameter is the step size which will affect how much it goes up by
print(new_string[::2])
# this case its going by 2

# will reverse a string
print(new_string[::-1])

# Immutability of strings
name = "Sam"

# name[0] = 'P' will not work

last_letters = name[1:]

print("P" + last_letters)

print(last_letters * 10)

# format()
print('This is a string {}'.format('INSERTED'))

print('The {} {} {}'.format('fox', 'brown', 'quick'))

# output the fox fox fox
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))

print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 100/77

# float formatting follows {value:width.precision f}
print('The result was {r:1.3f}'.format(r=result))

# f allows for format to be called
name = "Jose"
print(f'Hello his name is {name}')
