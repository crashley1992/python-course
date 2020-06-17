#while and else can be COMBINED
x = 0
while x < 5:
    print(f'the current value of x is {x}')
    x = x + 1
    x +=1
else: 
    print("X IS NOT LESS THAN 5")

    #break: breaks out of the current closest enclosing loop
    #continue: goes to the top of the closest enclosing loop
    #pass: does nothing at all

    x = [1,2,3]
    for item in x:
        #comment or place holder here. program will still run with pass to let you keep building out function
        pass

    mystring = 'Sammy'
    for letter in mystring:
        if letter == 'a':
             continue
        print(letter)


    mystring2 = 'Mammy'
    for letter in mystring:
        if letter == 'a':
             break
        print(letter)

#other useful operators
mylist2 = [1,2,3]
for num in range(10):
    print(num)

#out put will show index position for each letter
#At index 0 the letter is a

index_count =  0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count +=1

#enumerate will print out index with letter in the form of a tuple
word = 'abc'
for index,letter in enumerate(word):
    print(item)

#zip function will put two lists together output:
# (1, 'a')
# (2, 'b')
# (3, 'c')

list1 = [1,2,3]
list2 = ['a', 'b', 'c']

for item in zip(list1, list2):
    print(item)
