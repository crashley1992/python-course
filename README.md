# python-course
learning python/django

Python Data Types

- integers: int whole numbers
- floating points: float, numbers with decimal points
- strings: str ordered sequences of strings
- booleans: bool logical value indicating true or false

Data Structure:  
- lists: list ordered sequences of objects [10, "hello"]
- dictionaries: unordered key value pairs {"mykey" : "values, "names", "Frankie"}
- Tuples: tup ordered immutable sequence of objects (1, "hello", 12)
- Sets: unordered collection of unique objects {"a", "b","c"}


Lists:
-Lists are ordered sequences that can hold a vareity of object types 
- They use [] brackets and commas to separate objects in the list
- Lists support indexing and slicing. 
-Lists can be nested and also have a variet of useful methods

Dictionaries:
- Unordered mappings for storing objects.
- This key-value pir allow users to quickly grab objects wiwthout needing to know an index location

Dictionaries vs Lists
Dictionaries are objects retrived by keyname

lists are objects retrived by location and order sequence can be indexed or sliced.

Tuples
- Are similar to lists, but are immutable.
- Once as element is inside a tuple it cannot be reassigned.

Sets
- unordered collections of unique elements
- they can only be one represenative of the same object

Chaining comparison operators
- We can use logical operators to combine comparisons:

- and
- or
- not

Control Flow allows you to execute code only when a particular condition is met

- if
-elif
-else

Methods
Are functions that are built into objects

Lambada: A small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

ex: x = lambda a: a + 10
print(x(5))

LEGB RULE:
L: local - Names assigned in any way within a dunction def or lambda and not declared global in that function
E: Enclosing function locals -  Names in the local scope of any and all enclosing functions (def or lambda) from inner to outer.
G: Global (module) - names assigned at the top-level of module file, or declare global in a def within the file
B: Built in (Python) - Names preassigned in the built-in names module: open, range, Syntax Error

OOP 
- allows programmers to create their own objects that have methods and attributes.
-recall that after defining a string, list, dictionary, or other objects, you were able to call methods off of them with the .method_name() syntax
-classes are CamelCase

PyPi 
- is a repository for open-source third party Python Packages
- it's similar to rubygems in ruby work, and npm for node.js

use pip install to install packages

ex: pip install requests

Error handling:
try - this is the block of code to be attempted
except - block or code will execute in case there is an error in try block
finally - A final block of code to be executed regardless of an error

Testing tools:
Pylint - libary that looks at code and reports back issues

unittest: built in library will allow to test your own programs and check if you are getting desired outputs

Decorators:
- allows you to tack on extra functionality to an alrady existing function
- they use the @ operator and are then placed on top the original funcition.

Generator functions:
- allows us to write a function that can send back a value and then later resume to pick up where it left off
- generates a sequence of values over time
- use of yeild keyword

Collections:
- 