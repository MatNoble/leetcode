#==================================================
#==>      Title:                                     
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 
#==================================================

while True:
    try:
        from collections import Counter
        n = int(input())
        nums = list(map(int, input()))
        if n & 1:
            i, j = n//2 - 1, n//2 + 1
        else:
            i, j = n//2 - 1, n//2
        d = Counter(nums)
        dl = Counter(nums[:i+1])
        dr = Counter(nums[j:])
        res = dl[0] + dr[1] # 左 1 右 0
        res0 = d[1]   # 全 0
        res1 = d[0]   # 全 1
        print(min(res, res0, res1))
    except:
        break
