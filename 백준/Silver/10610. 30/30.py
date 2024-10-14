N = str(input())

if not '0' in N or sum(map(int, N)) % 3 != 0 :
    print(-1)
    exit()

print(''.join(sorted(N, reverse=True)))