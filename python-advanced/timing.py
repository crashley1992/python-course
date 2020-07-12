def func_one(n):
    return [str(num) for num in range(n)]

func_one(10)

def func_two(n):
    return list(map(str,range(n)))

func_two(10)

import time
# current time
start_time = time.time()
# run code
restult = func_one(100000)
# current time after running code
end_time = time.time()
# elapsed time
elapsed_time = end_time - start_time
print(elapsed_time)

import timeit
timeit.timeit
stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt,setup, number=100000))

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt2,setup2, number=100000))
