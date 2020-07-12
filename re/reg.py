# reg expression allows us to search for general patterns in text data
# re libary allows for specialized strings

text = "The agent's phone is 409-555-1234. Call Soon!"
import re
pattern = 'phone'
print(re.search(pattern,text))
# output provides index position 
# <re.Match object; span=(12, 17), match='phone'>
text =  'My phone numbe is 408-555-1234'
phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
results.group()
# give back first 3 digits
results.group(1)

# search for cat or dog
re.search(r'cat|dog', 'The cat is here')
# . is a wild card that will return whatever letter is infront of "at"
re.findall(r'.at', 'The cat in the hat sat there')
# ^ starts with
re.findall(r'^\d', '1 is a number')
# $ is ends with
re.findall(r'\d$', 'The number is 2')


# exculustion is used to remove puncuation from a sentance
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+'
print(re.findall(pattern,phrase))

# ^ following terms will show what to exclude. For example below !.? will be removed
test_phrase = "This is a string! But it has punctuation. How can we remove it?"
re.findall(r'[^!.?+]', test_phrase)

text = "only find the hypen-in this sentance. But you dont know how long-sih they are"
# looks for alpha numeric patters aka the -
pattern = r'[\w]+-[\w]+'
print(re.findall(pattern, text))
