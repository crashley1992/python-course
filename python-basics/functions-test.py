# Warm up section
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers 
# if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a and b % 2 == 0:
        if a > b:
            print(b)
            return(b)
        else: 
            print(a)
            return(a) 

# lesser_of_two_evens(3,2)

# ANIMAL CRACKERS: Write a function takes a two-word string 
# and returns True if both words begin with same letter

def animal_crackers(text):
    word_list = text.split()
    return word_list[0][0] == word_list[1][0]
    
# animal_crackers("hi hello")

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False¶
def makes_twenty(a,b):
    if a + b == 20:
        print('true')
        return True
    else:
        print('false')
        return False

# makes_twenty(10,10)

# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶
def myfunc(name):
    if len(name) > 3:
        print(name[:3].capitalize() + name[3:].capitalize())
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        print("name too short")
        return "name too short"   

# myfunc('ashley')

# MASTER YODA: Given a sentence, return a sentence with the words reversed¶
def yoda(str):
    ''.join(str.split()[::-1])    

yoda('i am home')

# ALMOST THERE: Given an integer n, 
# return True if n is within 10 of either 100 or 200
def num_range(n):
    return((abs(100 - n) <=10) or (abs(200-n) <=10))

num_range(90)

# Given a list of ints, return True if the array contains 
# a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i + 2]:
            return True

has_33([1,3,3])