class Solution:
    # @param A : list of integers
    # @return an integer
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def firstMissingPositive(self, A):
        least_negative_index = 0
        for ind,val in enumerate(A):
            if val > 0:
                A[least_negative_index],A[ind]=A[ind],A[least_negative_index]
                least_negative_index+=1
        for i in range(least_negative_index):
            mark_ind = abs(A[i])-1
            if mark_ind < least_negative_index:
                A[mark_ind] = -1 * abs(A[mark_ind])
        for i in range(least_negative_index):
            if A[i] > 0:
                return i+1
        return least_negative_index+1
                