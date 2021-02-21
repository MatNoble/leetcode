#==================================================
#==>      Title:                                     
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 
#==================================================


from typing import List
from collections import Counter
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dis(a, b):
            return (a[0]-b[0])**2+(a[1]-b[1])**2
        count = 0
        for a in points:
            dis_ = []
            for b in points:
                dis_.append(dis(a, b))
            dict = Counter(dis_)
            for val in dict.values():
                if val > 1:
                    count += val * (val-1)
        return count

mat = Solution()
points = [[1,1]]
points = [[0,0],[1,0],[2,0]]
# points = [[1,1],[2,2],[3,3]]
mat.numberOfBoomerangs(points)
