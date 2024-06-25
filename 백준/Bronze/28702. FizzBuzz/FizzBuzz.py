
FIZZ = 'Fizz'
BUZZ = 'Buzz'
FIZZBUZZ = FIZZ + BUZZ

a = input()
b = input()
c = input()

if a == FIZZ :
    if b == BUZZ :
        print(FIZZ)
    else :
        d = int(b) + 2
        if d % 15 == 0 :
            print(FIZZBUZZ)
        else :
            print(FIZZ)
elif a == BUZZ :
    if b == FIZZ :
        print(int(c) + 1)
    else :
        d = int(b) + 2
        if d % 3 == 0 :
            print(FIZZ)
        else :
            print(d)
elif a == FIZZBUZZ :
    print(FIZZ)
else :
    d = int(a) + 3
    if d % 15 == 0 :
        print(FIZZBUZZ)
    elif d % 5 == 0 :
        print(BUZZ)
    elif d % 3 == 0 :
        print(FIZZ)
    else :
        print(d)