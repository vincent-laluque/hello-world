print("Boo")
k = 1
while k < 21 :
    mul = k * 7     
    k = k + 1
    if (mul%3 == 0):
        print(mul, "*", end=' ')
    else:
        print(mul, end=' ')

print('\n')

k = 1
while k < 51 :
    mul = k * 13
    k = k + 1
    if (mul%7 == 0):
        print(mul, "*", end =' ')
    else:
        print(mul, end = ' ')

print('\n')

k = 1
while k < 8 :
    print(k*"*", end = '\n\n')
    k = k + 1
