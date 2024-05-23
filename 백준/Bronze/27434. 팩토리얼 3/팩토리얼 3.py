import sys
sys.setrecursionlimit(10 ** 9)

def fac(i) :
    if i == 1 or i == 0 :
        return 1
    return fac(i-1) * i

print(fac(int(input())))