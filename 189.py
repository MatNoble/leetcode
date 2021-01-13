#==================================================
#==>      Title:                                     
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 
#==================================================


nums = list(range(1, 8))
k = 3 + len(nums)

# nums = [-1,-100,3,99]
# k = 2
k %= len(nums)
print(k)

print(nums[-k:] + nums[:-k])
