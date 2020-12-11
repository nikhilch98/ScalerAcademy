class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        if len(A) == 1:
            return 0
        minAdd,maxAdd,minSub,maxSub=A[0],A[0],A[0],A[0]
        for i,val in enumerate(A):
            minAdd = min(minAdd,val+i)
            maxAdd = max(maxAdd,val+i)
            minSub = min(minSub,val-i)
            maxSub = max(maxSub,val-i)
        return max(maxAdd-minAdd,maxSub-minSub)