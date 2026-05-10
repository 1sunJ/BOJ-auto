def oper(a, b) :
    return int(str(a) + str(b))

def solution(a, b):
    res1 = oper(a, b)
    res2 = 2 * a * b
    return res1 if res1 >= res2 else res2