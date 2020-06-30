# Functions and Methods Homework
# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    volume = (4/3) * (3.14) * (rad**3)
    print(volume)

vol(2)

# course solutions
# def vol(rad):
#     return (4/3)*(3.14)*(rad**3)


# Write a function that checks whether a 
# number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    if num > low and num < high:
        print(True)
        return True
    else: 
        print(False)
        return False

ran_check(5,2,7)

# course solutions
# def ran_check(num,low,high):
#     #Check if num is between low and high (including low and high)
#     if num in range(low,high+1):
#         print('{} is in the range between {} and {}'.format(num,low,high))
#     else:
#         print('The number is outside the range.')


# Write a Python function that accepts a string and calculates the number
#  of upper case letters and lower case letters.
def up_low(s):
    upper_case = 0
    lower_case = 0
    for letter in s:
        if letter.isupper():
            upper_case += 1
            # print(upper_case)
        elif letter.islower():
            lower_case += 1
            # print(lower_case)
        else:
            pass
    print(upper_case)
    print(lower_case)

up_low('HelLo')

# course solutions
# def up_low(s):
#     d={"upper":0, "lower":0}
#     for c in s:
#         if c.isupper():
#             d["upper"]+=1
#         elif c.islower():
#             d["lower"]+=1
#         else:
#             pass
#     print("Original String : ", s)
#     print("No. of Upper case characters : ", d["upper"])
#     print("No. of Lower case Characters : ", d["lower"])


# Write a Python function that takes a list and returns a new list
#  with unique elements of the first list.
def unique_list(lst):
    new_list = list(dict.fromkeys(lst))
    print(new_list)

unique_list(['a','a','b','c','e','d','c'])
unique_list([1,2,3,4,4,4])

# course solution
# def unique_list(lst):
#     # Also possible to use list(set())
#     x = []
#     for a in lst:
#         if a not in x:
#             x.append(a)
#     return x

# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    result = 1
    for num in numbers:
        result = result * num
        print(result)

# multiply([1,2,3,4])

# course solutions

# def multiply(numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return total

# Write a Python function that checks whether a word or phrase is 
# palindrome or not.
def palindrome(s):
    if s == s[::-1]:
        print('palindrome')
    else: 
        print('not a palindrome')

palindrome('kayak')

# course solutions
# def palindrome(s):
    
#     s = s.replace(' ','') # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
#     return s == s[::-1]   # Check through slicing

# Write a Python function to check whether a string is pangram or not. 
# (Assume the string passed in does not have any punctuation)
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    for letter in str1:
        for x in alphabet:
            if letter == x:
                print('pangram')
                
ispangram('nurses run')

# course solutions

# import string

# def ispangram(str1, alphabet=string.ascii_lowercase): 
#     # Create a set of the alphabet
#     alphaset = set(alphabet)  
    
#     # Remove spaces from str1
#     str1 = str1.replace(" ",'')
    
#     # Lowercase all strings in the passed in string
#     # Recall we assume no punctuation 
#     str1 = str1.lower()
    
#     # Grab all unique letters in the string as a set
#     str1 = set(str1)
    
#     # Now check that the alpahbet set is same as string set
#     return str1 == alphaset