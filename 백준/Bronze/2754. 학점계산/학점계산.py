a=list(input())
b=False
if len(a)==2:
    a,b=a
if a=='A':
    a=4
elif a=='B':
    a=3
elif a=='C':
    a=2
elif a=='D':
    a=1
else:
    a=0
if b=='+':
    a+=0.3
if b=='-':
    a-=0.3

print(float(a))