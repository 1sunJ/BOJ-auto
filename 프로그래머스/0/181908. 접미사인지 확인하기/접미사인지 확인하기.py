def solution(my_string, is_suffix):
    a = my_string[::-1]
    b = is_suffix[::-1]
    return int(a.startswith(b))