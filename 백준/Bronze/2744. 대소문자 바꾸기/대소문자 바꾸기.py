arr=input()
for x in arr :
    print(x.upper() if x.islower() else x.lower(),end='')