"""Given two sorted arrays of size n and m respectively, find their union. The Union of two arrays can be defined as the common and distinct elements in the two arrays. Return the elements in sorted order.

Example 1:

Input: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 5, arr2 [] = {1, 2, 3, 6, 7}
Output: 
1 2 3 4 5 6 7
Explanation: 
Distinct elements including both the arrays are: 1 2 3 4 5 6 7.
Example 2:

Input: 
n = 5, arr1[] = {2, 2, 3, 4, 5}  
m = 5, arr2[] = {1, 1, 2, 3, 4}
Output: 
1 2 3 4 5
Explanation: 
Distinct elements including both the arrays are: 1 2 3 4 5.
Example 3:

Input:
n = 5, arr1[] = {1, 1, 1, 1, 1}
m = 5, arr2[] = {2, 2, 2, 2, 2}
Output: 
1 2
Explanation: 
Distinct elements including both the arrays are: 1 2.
Your Task: 
You do not need to read input or print anything. Complete the function findUnion() that takes two arrays arr1[], arr2[], and their size n and m as input parameters and returns a list containing the union of the two arrays.

Expected Time Complexity: O(n+m).
Expected Auxiliary Space: O(n+m).

Constraints:
1 <= n, m <= 105
-109 <= arr1[i], arr2[i] <= 109
"""






# SOLUTION:

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
       
        res = []
        i = 0
        j = 0
        
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if not res or res[-1] != arr1[i]:
                    res.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if not res or res[-1] != arr2[j]:
                    res.append(arr2[j])
                j += 1
            else:
                if not res or res[-1] != arr1[i]:
                    res.append(arr1[i])
                i += 1
                j += 1
                
  
        while i < n:
            if not res or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
        
       
        while j < m:
            if not res or res[-1] != arr2[j]:
                res.append(arr2[j])
            j += 1
        
        return res
