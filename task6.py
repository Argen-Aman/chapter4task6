list_ = input('Type some symbols(don\'t forget spaces):\n').split()
value_ = int(input('Type value for shifting previous list: '))
print()

list_2 = list_.copy()

i = 0
if value_ > 0:
    print('To trick your enemies, we will print a lot of ciphers...')
    while i < value_:
        i += 1
        a = list_2.pop()
        b = list_2.insert(0, a)
        print(list_2)
    print('Your analogue for Caesar\'s cipher is the last one.')
elif value_ < 0:
    print('To trick your enemies, we will print a lot of ciphers...')
    while i < abs(value_):
        i += 1
        x = list_2.pop(0)
        y = list_2.append(x)
        print(list_2)
    print('Your analogue for Caesar\'s cipher is the last one.')
else:
    print(list_)
    print('Unfortunately, your analogue for Caesar\'s cipher remain unchanged.')
