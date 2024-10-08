class Solution:
    
    def getSecondLargest(self, arr):
        # Code Here
        largest = None
        second = None
        for num in arr:
            if largest is None or num > largest:
                second = largest
                largest = num
            
            elif num != largest and (second is None or num > second):
                second = num
                
        return second if second is not None else -1
