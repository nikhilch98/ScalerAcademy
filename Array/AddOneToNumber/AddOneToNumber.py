class Solution:
    # @param A : list of integers
    # @return a list of integers
    # Time Complexity  : O(n)
    # Space Complexity : O(1)
    def plusOne(self, A):
        carry = 1
        left_significant_index = len(A)-1
        for i in range(len(A)-1,-1,-1):
            A[i],carry=(A[i]+carry)%10,(A[i]+carry)//10
            if A[i]!=0:
                left_significant_index = i
        if carry == 1:
            A = [1]+A
        else :
            A = A[left_significant_index:]
        return A