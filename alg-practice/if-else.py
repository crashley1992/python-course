def numbers(n):
    if n % 2 != 0:
        print(f'Weird {n}')
    elif n in range(2,6):
        if n % 2 == 0:
            print('Not Weird')
    elif n in range(6,21):
        if n % 2 == 0:
            print(f'Weird {n}')
    elif n > 20 and n % 2 == 0:
        print(f'Not Weird {n}')

numbers(3)
