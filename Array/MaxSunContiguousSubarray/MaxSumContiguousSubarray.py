class Solution:
    # @param A : tuple of integers
    # @return an integer
    # Time Complexity  : O(n)
    # Space Complexity : O(1)
    def maxSubArray(self, A):
        res = A[0]
        temp = A[0]
        for val in A[1:]:
            temp = max(val,temp+val)
            res = max(temp,res)
        return res