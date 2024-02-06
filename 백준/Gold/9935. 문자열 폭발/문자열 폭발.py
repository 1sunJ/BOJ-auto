str1 = list(input())
str2 = list(input())
len2 = len(str2)

que = []

for x in str1 :
    que.append(x)

    if que[-len2::] == str2 :
        for _ in range(len2) :
            que.pop()

if que :
    print(*que, sep = '')
else :
    print("FRULA")