# # python debugger
# x = [1,2,3]
# y = 2
# z = 3

# result = y + z
# # error because list will not add to a number
# result2 = x + y

# imports python debugger
import pdb

x = [1,2,3]
y = 2
z = 3

result_one = y + z

pdb.set_trace()
result_two = x + y

