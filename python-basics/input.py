# using text file
myfile = open('test.txt')
print(myfile.read())

# will reset reading to 
myfile.seek(0)