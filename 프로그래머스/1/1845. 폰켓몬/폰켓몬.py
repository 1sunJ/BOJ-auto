def solution(nums):
    # nums 개수 /2 를 한다.
    l = len(nums) // 2
    
    # set(nums)를 해서 개수를 센다
    s = set(nums)
    num = len(s)

    # set(nums)개수가 nums 개수 l 보다 크면 nums 개수 2반환 
    if num > l :
        return l
    else :
        return num 
    # 아니면 set(nums) 개수 반환 