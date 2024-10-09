class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        for i in range(N):
            if K == arr[i]:
                return 1
        
        return -1
