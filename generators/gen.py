def create_cubes(n):
# generates value as needed. Since it's printing 1 num on a line a gen would take less memory
    for x in range(n):
        yield x**3
    
for x in create_cubes(10):
    print(x)


def gen_fibon(n):

    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a + b

for number in gen_fibon(10):
    print(number)


# next()
def simple_gen():
    for x in range(3):
        yield x
    
    for x in simple_gen():
        print(number)

g = simple_gen()
print(next(g))

# iter()
s = 'hello'

for letter in s:
    print(letter)

s_iter = iter(s)
print(s_iter)
print(next(s_iter))