import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    strs = list(input().split())

    for s in strs : 
        print("".join(list(s)[::-1]), end = ' ')
    print()