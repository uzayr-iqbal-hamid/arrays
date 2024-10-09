class Solution:
    def largest(self, arr : List[int]) -> int:
        max = 0
        for num in arr:
            if num > max:
                max = num
        
        return max

# Alternate solution, more efficient

class Solution:
    def largest(self, arr : List[int]) -> int:
        return reduce(lambda x, y: x if x > y else y, arr)
