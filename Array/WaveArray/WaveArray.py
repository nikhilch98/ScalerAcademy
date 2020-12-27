class Solution:
	# @param A : list of integers
	# @return a list of integers
    # Time complexity : O(nlogn)
    # Space Complexity : O(1)
	def wave(self, A):
        A.sort()
        for i in range(1,len(A),2):
            A[i],A[i-1]=A[i-1],A[i]
        return A
            