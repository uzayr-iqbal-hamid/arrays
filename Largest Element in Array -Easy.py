class Solution:
    def largest(self, arr : List[int]) -> int:
        # code here
        max = 0
        for num in arr:
            if num > max:
                max = num
        
        return max
