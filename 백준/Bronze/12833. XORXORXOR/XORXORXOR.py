A, B, C = map(int, input().split())

for _ in range(C % 2) :
    A = A ^ B

print(A)