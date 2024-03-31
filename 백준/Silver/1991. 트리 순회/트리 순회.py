def preorder(crt) :
    if crt == '.' :
        return
    crt = nodes[crt]
    print(crt[0], end = '')
    preorder(crt[1])
    preorder(crt[2])

def inorder(crt) :
    if crt == '.' :
        return
    crt = nodes[crt]
    inorder(crt[1])
    print(crt[0], end = '')
    inorder(crt[2])
    
def postorder(crt) :
    if crt == '.' :
        return
    crt = nodes[crt]
    postorder(crt[1])
    postorder(crt[2])
    print(crt[0], end = '')

N = int(input())

nodes = {}
for i in range(65, 65 + N) :
    nodes[chr(i)] = [0] * 3
    nodes[chr(i)][0] = chr(i)

for _ in range(N) :
    a, b, c = input().split()
    nodes[a][1] = b
    nodes[a][2] = c

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()