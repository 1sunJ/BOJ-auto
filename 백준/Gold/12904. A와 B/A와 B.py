A = list(input())
B = list(input())

while len(A) < len(B) :
    if B[-1] == 'A' :
        B.pop()
    else :
        B.pop()
        B = B[::-1]

print(int(A == B))