# Chaining comparison operators
print(1 < 2)

# returns false because 2 is less than 3
print(1 < 2 > 3)

# And is asking is whats on my left true and whats on my right true
print(1 < 2 and 2 < 3)

print('h' == 'h' and 2 == 2 )

print(1 == 1 or 2 == 2)

# Control flow
# For loops in Python
my_list = [1 ,2, 3, 4, 5]

# for num in my_list:
#     print(num)

for num in my_list:
    if num % 2 == 0:
        print(num)
        for num in my_list:
            if num % 2 == 1:
                print("odd")

# prints list
new_list = [(1,2), (3,4)]
for item in new_list:
        print(item)

#prints individual items in list
for (a,b) in new_list:
    print(a)
    print(b)

# dictionary
d = {'k1':1 , 'k2':2}

for item in d:
    print(item)

# output 1 and 2
for key,value in d.items():
    print(value)

my_list3 = [letter for letter in "greetings"]
print(my_list3)

my_list3 = [num for num in range(0,11)]
print(my_list)

my_list4 = [x for x in range(0,11) if x % 2 ==0]
print(my_list4)

my_list5= []
for x in [2,4,6]:
    for y in [100,200,300]:
        my_list5.append(x*y)
